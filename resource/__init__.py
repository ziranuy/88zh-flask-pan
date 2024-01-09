# -*- coding: utf-8 -*-
# @Time    : 2024/1/6
# @Author  : lhq
# @File    : __init__.py.py
# @Description :

proxies = {
    'http':'http://127.0.0.1:10809',
    'https':'http://127.0.0.1:10809',
}





'''
def wpxz(keyword):

    cookies = {
        'flarum_session': '74BgMw4kRuQft5XbXgm6nfKiuOugTcsnKBX4lWBg',
        '__51vcke__K7r5x69JaxwZOOJp': '8c0e1ec6-c815-5124-9f9d-6593bde2a56e',
        '__51vuft__K7r5x69JaxwZOOJp': '1704541903585',
        '__vtins__K7r5x69JaxwZOOJp': '%7B%22sid%22%3A%20%223f207794-bd18-5df5-86b5-d8394edb2d19%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201704551194194%2C%20%22ct%22%3A%201704549394194%7D',
        '__51uvsct__K7r5x69JaxwZOOJp': '2',
        'cf_clearance': 'iHiwAf_GwthaUEPixZE5qgbQgWion37AfNhmn.g1sKc-1704549399-0-2-c2370dda.9e668fec.9536523a-250.0.0',
    }

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

    response = requests.get('https://wpxz.top/', params=params,cookies=cookies, headers=headers,proxies=proxie).text
    print(response)
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



'''