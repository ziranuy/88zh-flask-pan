# -*- coding: utf-8 -*-
# @Time    : 2024/1/4
# @Author  : lhq
# @File    : app.py
# @Description :
import json

import redis
from flask import Flask,  request
from flask_cors import CORS

from resource.pan99 import  pan99
from resource.yunpan1 import yunpan1
from resource.yunpanziyuan import yunpanziyuan
from utils.response import response_decorator

app = Flask(__name__)
CORS(app)

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


@app.route('/api/tabs_list', methods=['GET'])
@response_decorator
def tabs_list():
    return ['云盘资源&yunpanziyuan', '盘99&pan99','云盘1&yunpan1']


@app.route('/api/get_list', methods=['GET'])
@response_decorator
def get_list():
    keyword = request.args.get('keyword')
    active_name = request.args.get('activeName')
    print(keyword,active_name)
    r_keyword = keyword + active_name
    result = [{'title': '没有找到内容', 'url': 'https://www.baidu.com'},
              {'title': '没有找到内容', 'url': 'https://www.baidu.com'}]
    if keyword is None:
        return result

    # 获取键的值
    r_data = r.get(r_keyword)
    if r_data is not None:
        return json.loads(r_data)

    if active_name == 'yunpanziyuan':
        result = yunpanziyuan(keyword)
    elif active_name == 'pan99':
        result = pan99(keyword)
    elif active_name == 'yunpan1':
        result = yunpan1(keyword)

    r.set(r_keyword, json.dumps(result))
    # 过期时间 4个小时
    r.expire(r_keyword, 14400)

    return result


if __name__ == '__main__':
    app.run(debug=True)

'''
result = [
        {
            "title": "🐻🐻[繁花]🐻🐻（沪语+普通话版更新中）(胡歌.马伊琍.唐嫣.辛芷蕾)繁花繁花繁花繁花 夸克网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-226215.htm"
        },
        {
            "title": "🔥繁花🔥4K最新🔥王家卫导演胡歌马伊琍繁花繁花繁花 AL云盘 夸克网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-226198.htm"
        },
        {
            "title": "繁花4K(2023)🔥今日更新最新一集🔥胡歌/马伊琍/唐嫣/游本昌/🔥繁花导演：王家卫 AL云盘 百度网盘 夸克网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-226211.htm"
        },
        {
            "title": "繁花 （2023）首播 夸克网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-226224.htm"
        },
        {
            "title": "繁花似锦(2023)爱情都市剧情 AL云盘 夸克网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-138576.htm"
        },
        {
            "title": "繁花（2023）剧情/爱情，胡歌、马伊琍主演 夸克网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-226209.htm"
        },
        {
            "title": "繁花 (2023) 新增4K杜比  上传中 请期待  百度网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-226231.htm"
        },
        {
            "title": "繁花 (2023) 剧情 / 爱情 胡歌 / 马伊琍 / 唐嫣 汉语普通话 / 沪语 AL云盘 夸克网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-226386.htm"
        },
        {
            "title": "🔥🔥【繁花/王家卫导演/胡歌 唐嫣 马伊琍】30集持续更新中🔥🔥 AL云盘",
            "url": "https://www.yunpanziyuan.xyz/thread-226200.htm"
        },
        {
            "title": "电视剧海上繁花高清视频在线观看，百度网盘下载 百度网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-115469.htm"
        },
        {
            "title": "?繁花似锦(2023)爱情4K60帧?关注我持续更新 AL云盘 夸克网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-138577.htm"
        },
        {
            "title": "[PC/解谜冒险]地铁繁花 v1.1.10免安装中文版[148M/度盘] 百度网盘",
            "url": "https://www.yunpanziyuan.xyz/thread-194113.htm"
        }
    ]
'''
