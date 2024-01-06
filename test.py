# from DrissionPage import ChromiumPage
#
# from DrissionPage import ChromiumOptions
# from DrissionPage.configs.session_options import SessionOptions
#
# #
# so = SessionOptions()
# # 设置代理
# so.set_proxies('http://localhost:10809')
# co = ChromiumOptions()
# co.set_paths(user_data_path=None)
#
# page = ChromiumPage()
# page.get('https://wpxz.top/?q=%E7%B9%81%E8%8A%B1')
# iframe = page.get_frame('@src^https://challenges.cloudflare.com/cdn-cgi',timeout=7)
# if iframe:
#     iframe('.ctp-checkbox-label').click()
# print(page.html)
#
# page.quit()



import time
import re
import math
from DrissionPage import ChromiumPage
from DrissionPage.easy_set import set_paths
from DrissionPage import ChromiumOptions
from DrissionPage.easy_set import set_headless, set_paths
# set_headless(True)
#
# #必须要加这个 表示在linux上无头加载
# co = ChromiumOptions()
# co.set_argument('--incognito')
# co.set_argument('--no-sandbox')
#set_paths(browser_path=r'/opt/google/chrome/google-chrome')
#set_paths(browser_path=r'C:/Users/AAA/AppData/Local/Google/Chrome/Application/chrome.exe')
page = ChromiumPage()
page.get('https://wpxz.top/?q=%E7%B9%81%E8%8A%B1')
if '请稍候…' in page.html:
    time.sleep(8)

# iframe = page.get_frame('@src^https://challenges.cloudflare.com/cdn-cgi',timeout=10)
# if iframe:
#     iframe('.ctp-checkbox-label').click()
print(page.html)
#关闭浏览器
page.close_tabs()
