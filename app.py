# -*- coding: utf-8 -*-
# @Time    : 2024/1/4
# @Author  : lhq
# @File    : app.py
# @Description :

from flask import Flask, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/yunpanziyuan')
def yunpanziyuan():

    cookies = {
        'bbs_sid': 'dgjkdkn6degfq4nd3v0nr45i7a',
        'isClose': 'yes',
    }
    
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.yunpanziyuan.xyz/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    
    params = {
        'fontname': '繁花',
    }
    
    response = requests.get('https://www.yunpanziyuan.xyz/fontsearch.htm', params=params, cookies=cookies, headers=headers).text


    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
