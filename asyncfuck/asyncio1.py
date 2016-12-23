# encoding: utf-8
"""
@version: ??
@author: lizheao
@contact: lizheao940510@gmail.com
@software: PyCharm
@file: asyncio1.py
@time: 17:11
"""
#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永无BUG
import asyncio
import time

import aiohttp
import requests

NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'


def fetch(a):
    r = requests.get(URL.format(a))
    return r.json()['args']['a']


async def fetch_async(a):
    async with aiohttp.request('GET', URL.format(a)) as r:
        data = await r.json()
    return data['args']['a']


# async def run_scraper_tasks(executor):
#     loop = asyncio.get_event_loop()
#     blocking_tasks = []
#     for num in NUMBERS:
#         task = loop.run_in_executor(executor, fetch, num)
#         task.__num = num
#         blocking_tasks.append(task)
#     completed, pending = await asyncio.wait(blocking_tasks)
#     results = {t.__num: t.result() for t in completed}
#     for num, result in sorted(results.items(), key=lambda x: x[0]):
#         print('fetch({}) = {}'.format(num, result))
start = time.time()
event_loop = asyncio.get_event_loop()
tasks = [fetch_async(num) for num in NUMBERS]
results = event_loop.run_until_complete(asyncio.gather(*tasks))
for num, result in zip(NUMBERS, results):
    print('fetch({}) = {}'.format(num, result))
print('Use asyncio+requests+ThreadPoolExecutor cost: {}'.format(time.time() - start))
