from selenium import webdriver
import time

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
# browser = webdriver.Chrome(executable_path=(r'..\chromedriver.exe'), options=chrome_options)
browser = webdriver.Chrome(options=chrome_options)


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
    time.sleep(1)
    # get sms code
    name = input('sms code：')
    print(name)
    browser.find_element(by=By.TAG_NAME, value="input").send_keys(name)
    time.sleep(1)
    browser.find_element(by=By.CLASS_NAME, value="m-btn").click()

    # 组装cookie字符串
    time.sleep(1)
    cookie_items = browser.get_cookies()
    build_cookies(cookie_items)
    import pdb
    pdb.set_trace()


def build_cookies(cookies_in: list) -> str:
    cookie_str = ""
    for item_cookie in cookies_in:
        item_str = item_cookie["name"] + "=" + item_cookie["value"] + "; "
        cookie_str += item_str
    with open("cookie.txt", "w") as f:
        f.write(cookie_str)
    return cookie_str


def get_sms_code():
    ...


def save_cookies():
    ...


if __name__ == '__main__':
    print("begin login")
    # 设置用户名、密码
    # username = '18765918310'
    # password = "song18765918310"
    # weibo_login(username, password)
    # build_cookies([])
