from DrissionPage import ChromiumPage
from DrissionPage import SessionOptions

so = SessionOptions()
# 设置代理
so.set_proxies('http://localhost:10809')


page = ChromiumPage()
page.get('https://wpxz.top/')