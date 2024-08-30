#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：yuanrenxue 
@File    ：run.py
@IDE     ：PyCharm 
@Author  ：Allen.Wan
@Date    ：2024/8/26 下午4:05 
@explain : 文件说明
"""
import json
import time

import requests

from levels.l1.md5_js_wrapper import MD5JSWrapper


def extract_value(resp):
    content = resp.text
    json_content = json.loads(content)
    data = json_content['data']
    sum = 0
    count = 0
    for item in data:
        value = item['value']
        sum += value
        count += 1
    return sum,count


total_page = 5
total_count = 0
page = 1

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1724141661,1724393610,1724401206,1724402399; HMACCOUNT=763A68441A9ED4BA; no-alert3=true; tk=-8915233993826486570; sessionid=t4h8f1tk7d5dya23ijjwr41rihu5oc5x; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1724142206,1724635189; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1724635189; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1724635192',
    'priority': 'u=0, i',
    'referer': 'https://match.yuanrenxue.cn/match/1',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    'x-requested-with': 'XMLHttpRequest'
}

payload = {}

total_sum = 0

while page <= total_page:
    long_time_stamp = int(time.time() * 1000)
    long_time_stamp = long_time_stamp - (long_time_stamp % 1000) + 100000000
    short_time_stamp = int(long_time_stamp / 1000)
    md5_wrapper = MD5JSWrapper(r'E:\SpiderProject\yuanrenxue\levels\l1\md5_mogai.js')

    # 调用 hex_md5
    md5_hash = md5_wrapper.hex_md5(str(long_time_stamp))
    url = f"https://match.yuanrenxue.cn/api/match/1?page={page}&m={md5_hash}%E4%B8%A8{short_time_stamp}"
    response = requests.request("GET", url, headers=headers, data=payload)
    page_sum, page_count = extract_value(response)
    total_sum += page_sum
    total_count += page_count
    page += 1

print("total sum is : " + str(total_sum / total_count))
