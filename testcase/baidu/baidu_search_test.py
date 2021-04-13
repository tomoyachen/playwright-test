import pytest
from playwright.async_api import Page, Dialog
from page.baidu.baidu_search_page import BaiduSearchPage
import time
from common.tools import Tools
import allure

class BaiduSearchTest:

    # 测试数据都存放在 fixtures
    @pytest.fixture()
    def fixtures(self):
        yield Tools.get_fixtures("baidu_search")


    @staticmethod
    @allure.title('百度搜索')
    def test_baidu_search(page: Page, env: dict, fixtures):
        """
        名称：百度搜索"playwright"
        步骤：
        1、打开浏览器
        2、输入"playwright"关键字
        3、点击搜索按钮
        检查点：
        * 检查页面标题是否相等。
        """

        baiduSearchPage = BaiduSearchPage(page)
        baiduSearchPage.open()
        baiduSearchPage.search_keywords(fixtures['kerwords'])
        time.sleep(2)
        assert baiduSearchPage.page.title() == f'{fixtures["kerwords"]}_百度搜索'
        assert 1 == 2


    @staticmethod
    @allure.title('百度搜索设置信息')
    def test_baidu_search_setting(page: Page):
        """
        名称：百度搜索设置
        步骤：
        1、打开百度浏览器
        2、点击设置链接
        3、在下拉框中"选择搜索"
        4、点击"保存设置"
        5、对弹出警告框保存
        检查点：
        * 检查是否弹出提示框
        """
        baiduSearchPage = BaiduSearchPage(page)
        baiduSearchPage.page.goto(baiduSearchPage.url)
        baiduSearchPage.page.click(baiduSearchPage.settings)
        baiduSearchPage.page.click(baiduSearchPage.search_setting)
        baiduSearchPage.page.click(baiduSearchPage.save_setting)

        def on_dialog(dialog: Dialog):
            assert dialog.type == "alert"
            assert dialog.message == "已经记录下您的使用偏好"
            dialog.accept()

        page.on("dialog", on_dialog)


    # Network events
    # ref: https://playwright.dev/python/docs/network#network-events
    @staticmethod
    def test_baidu_search_with_network(page: Page, env: dict, fixtures):
        """
        获取请求/ 响应
        """
        import re

        page.on("request",
                lambda request: print(">>", request.method, request.url) if not re.findall('.*/.[js|css|png]',
                                                                                           request.url) else None)
        page.on("response",
                lambda response: print("<<", response.status, response.url) if not re.findall('.*/.[js|css|png]',
                                                                                              response.url) else None)

        baiduSearchPage = BaiduSearchPage(page)
        baiduSearchPage.open()


if __name__ == '__main__':
    pytest.main(["-v", "-s"])
