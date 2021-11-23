import pytest
from playwright.async_api import Page, Browser, BrowserContext
from page.baidu.baidu_search_page import BaiduSearchPage
import time
from common.tools import Tools


# 利用 global 简化 page 使用
baiduSearchPage: BaiduSearchPage

class BaiduSearchTest:

    @pytest.fixture(scope="class", autouse=True)
    def before(self, page: Page):
        global baiduSearchPage
        baiduSearchPage = BaiduSearchPage(page)


    @pytest.fixture()
    def fixtures(self):
        yield Tools.get_fixtures("baidu_search")


    @staticmethod
    def test_baidu_search_with_multi_browser(page: Page, env: dict, fixtures, browser:Browser):

        baiduSearchPage.open()
        baiduSearchPage.search_keywords(fixtures['kerwords'])
        time.sleep(2)
        assert baiduSearchPage.page.title() == f'{fixtures["kerwords"]}_百度搜索'

        # 新开浏览器做另一件事
        # browser.new_page() 方式打开的浏览器是 sessions 不互通的
        page2 = browser.new_page(locale="zh-CN")
        baiduSearchPage2 = BaiduSearchPage(page2)
        baiduSearchPage2.open()
        baiduSearchPage2.search_keywords('我是新浏览器')
        time.sleep(2)
        page2.close() #由于是手动打开的，所以要自己关闭一下

    @staticmethod
    def test_baidu_search_with_multi_tab(page: Page, env: dict, fixtures, browser:Browser):

        # 新开浏览器打开2个tab
        # context.new_page() 方式打开的浏览器是 sessions 互通的，类似于打开多个选项卡
        page3:BrowserContext = browser.new_context(locale="zh-CN")
        page3_tab1:Page = page3.new_page()
        page3_tab2:Page = page3.new_page()

        page3_tab1.goto("https://www.baidu.com/s?wd=我是窗口 1")
        page3_tab2.goto("https://www.baidu.com/s?wd=我是窗口 2")
        time.sleep(2)
        page3.close()


if __name__ == '__main__':
    pytest.main(["-v", "-s"])
