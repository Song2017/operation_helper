import os

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

chrome_options = Options()
chrome_options.add_argument("--headless")
# browser = webdriver.Chrome(executable_path=(r'..\chromedriver.exe'), options=chrome_options)
browser = webdriver.Chrome(options=chrome_options)
_url = os.getenv("server_host")


# 登录微博
def weibo_login(username_in, password_in):
    # 打开微博登录页
    browser.get('https://passport.weibo.cn/signin/login')
    browser.implicitly_wait(5)
    time.sleep(1)
    # 填写登录信息：用户名、密码
    browser.find_element(value="loginName").send_keys(username_in)
    browser.find_element(value="loginPassword").send_keys(password_in)
    time.sleep(1)
    # 点击登录
    browser.find_element(value="loginAction").click()
    time.sleep(1)
    browser.find_element(by=By.CLASS_NAME, value="m-btn").click()
    time.sleep(5)

    # get sms code
    name = input('sms code：')
    print(name)

    browser.find_element(by=By.TAG_NAME, value="input").send_keys(name)
    time.sleep(5)
    browser.implicitly_wait(1)
    browser.find_element(by=By.CLASS_NAME, value="m-btn").click()
    time.sleep(1)
    browser.implicitly_wait(1)



def build_cookies(cookies_in: list) -> str:
    cookie_str = ""
    for item_cookie in cookies_in:
        item_str = item_cookie["name"] + "=" + item_cookie["value"] + "; "
        cookie_str += item_str
    with open("cookie.txt", "w") as f:
        f.write(cookie_str)
    return cookie_str


def get_sms_code():
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {os.getenv("bear_token")}',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", _url + "sms-authentication/?is_enabled=true", headers=headers)
    resp_data = response.json()
    print(resp_data)
    payload = {
        "type": "string",
        "platform": "weibo",
        "token": resp_data.get("token"),
        "is_enabled": False,
        "app_authentication_id": resp_data.get("app_authentication_id"),
    }
    response = requests.request("PUT", _url + "sms-authentication/", headers=headers, json=payload)
    print(response)
    return resp_data.get("token")


def get_content():
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {os.getenv("bear_token")}',
    }

    response = requests.request("GET", _url + "operation/?page_no=1&page_size=1&is_consumed=false", headers=headers)
    resp_data: list = response.json()
    print(resp_data)
    content = ",".join([item.get("content") for item in resp_data])
    for item in resp_data:
        payload = {
            "app_operation_info_id": item.get("app_operation_info_id"),
            "is_consumed": True
        }
        requests.request("PUT", _url + "operation/", headers=headers, json=payload)
    content = content.replace("@", "at")
    return content


def post_article(content_in: str):
    browser.implicitly_wait(5)
    if not content_in:
        content_in = get_content()
    browser.get('https://weibo.com')
    browser.implicitly_wait(3)

    try:
        browser.find_element(by=By.CSS_SELECTOR, value="div.lite-iconf.lite-iconf-releas").click()
    except Exception as e:
        print(str(e))
    browser.find_element(by=By.CSS_SELECTOR, value="textarea").send_keys(content_in)
    browser.implicitly_wait(3)
    try:
        browser.find_element(by=By.CSS_SELECTOR, value="div.wbpro-layer-tit-opt.woo-box-flex.woo-box-alignCenter.woo-box-justifyCenter").click()
    except Exception as e:
        print(str(e))


    browser.find_element(by=By.CSS_SELECTOR, value="button.woo-button-main").click()
    browser.implicitly_wait(3)


if __name__ == '__main__':
    print("begin login")
    # print(get_content())
    # 设置用户名、密码
    username = os.getenv("weibo_user")
    password = os.getenv("weibo_pass")
    weibo_login(username, password)
    # build_cookies([])
    # post article
    post_article("")

    # 组装cookie字符串
    cookie_items = browser.get_cookies()
    build_cookies(cookie_items)

    import pdb
    pdb.set_trace()    