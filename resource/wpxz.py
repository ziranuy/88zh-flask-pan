# -*- coding: utf-8 -*-
# @Time    : 2024/1/6
# @Author  : lhq
# @File    : wpxz.py
# https://wpxz.top/
# @Description :
import re

import requests


def wpxz(keyword):
    headers = {
        'authority': 'wpxz.top',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'zh-CN,zh;q=0.9',
    }

    params = {
        'q': keyword,
    }

    response = requests.get('https://wpxz.top/', params=params, headers=headers).text
    pattern = r'<noscript id="flarum-content">(.*?)>下一页'
    match = re.search(pattern, response, re.DOTALL)
    if match:
        obj1 = match.group(1)[:-40]
    else:
        return None

    pattern = r'<a href="(.*?)">\s*(.*?)\s*</a>'
    matches = re.findall(pattern, obj1, re.DOTALL)

    # 使用strip()函数删除字符串两端的空白字符
    matches = [(url, title.strip()) for url, title in matches]
    result = [{"title": title, "url": url} for url, title in matches]
    return result
