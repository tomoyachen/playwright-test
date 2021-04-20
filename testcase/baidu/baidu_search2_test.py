import pytest
from playwright.async_api import Page, Browser
from page.baidu.baidu_search_page import BaiduSearchPage
import time
from common.tools import Tools

# 利用 global 简化 page 使用
baiduSearchPage: BaiduSearchPage

class BaiduSearchTest:

    @pytest.fixture(scope="class", autouse=True)
    def page(self, browser: Browser):
        page = browser.new_page()
        global baiduSearchPage
        baiduSearchPage = BaiduSearchPage(page)
        yield page


    @pytest.fixture()
    def fixtures(self):
        yield Tools.get_fixtures("baidu_search")

    @staticmethod
    def test_baidu_search(page: Page, env: dict, fixtures):

        baiduSearchPage.open()
        baiduSearchPage.search_keywords(fixtures['kerwords'])
        time.sleep(2)
        assert baiduSearchPage.page.title() == f'{fixtures["kerwords"]}_百度搜索'

if __name__ == '__main__':
    pytest.main(["-v", "-s"])
