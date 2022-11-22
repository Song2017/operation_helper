import asyncio

import arrow
import requests
import concurrent.futures

url = "http://139.196.213.108:9003/api/operation/"


def create_operation(payload_in: str = ""):
    if not payload_in:
        return "content is None"
    data = {
        "name": payload_in[:5],
        "description": payload_in[:5],
        "content": payload_in
    }
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, json=data)
    return response.text


async def main(info_in: list):
    print(arrow.now())
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        loop_in = asyncio.get_event_loop()
        futures = [
            loop_in.run_in_executor(
                executor,
                create_operation,
                data
            )
            for data in info_in
        ]
        for response in await asyncio.gather(*futures):
            print(response)
    print(arrow.now())

if __name__ == '__main__':
    # payload = {
    #     "name": "string",
    #     "description": "string",
    #     "content": "string"
    # }
    #
    # create_operation(payload)
    data_info = ["大部分程序员沟通时都会带一些英文词，比如bug、issue、cpu、git、java…",
                 "你永远不能确定你的想法到底是不是独一无二的原创想法。", ]
    _loop = asyncio.get_event_loop()
    _loop.run_until_complete(main(data_info))
