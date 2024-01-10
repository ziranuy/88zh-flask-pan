# -*- coding: utf-8 -*-
# @Time    : 2024/1/10
# @Author  : lhq
# @File    : gitcafe.py
# @Description :
import requests



def gitcafe(keyword):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Accept': '*/*',
        'Origin': 'http://a.gitcafe.net',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'http://a.gitcafe.net/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data = {
        'action': 'search',
        'from': 'web',
        'token': '35a0c9468adef4eb993dc981e30ce07d9547c0',
        'keyword': keyword,
    }

    response = requests.post('https://gitcafe.net/tool/alipaper/', headers=headers, data=data).json()
    if not response.get('success'):
        return [{'title': '暂无资源', 'url': 'https://www.baidu.com'}]

    result = []
    for res in response.get('data'):
        result.append({
            'title': res.get('title'),
            'url': 'https://www.aliyundrive.com/s/' + res.get('alikey')
        })
    return result

