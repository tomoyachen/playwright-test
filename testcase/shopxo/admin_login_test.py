import pytest
from playwright.async_api import Page

class AdminLoginTest:

    @pytest.fixture(scope="class", autouse=True)
    def before(self, page: Page):
        page.goto("http://localhost/shopxo/admin.php")

    @staticmethod
    def test_admin_login(page: Page):
        """
        登录后台
        """
        # Click [placeholder="请输入用户名"]
        page.click("[placeholder=\"请输入用户名\"]")
        # Fill [placeholder="请输入用户名"]
        page.fill("[placeholder=\"请输入用户名\"]", "admin")
        # Fill [placeholder="请输入登录密码"]
        page.fill("[placeholder=\"请输入登录密码\"]", "shopxo")
        # Click button:has-text("登录")
        page.click("button:has-text(\"登录\")")
        # Go to http://localhost/shopxo/admin.php?s=/index/index.html
        page.goto("http://localhost/shopxo/admin.php?s=/index/index.html")

        assert page.url == 'http://localhost/shopxo/admin.php?s=/index/index.html'

    @staticmethod
    def test_admin_click_menu(page: Page):
        """
        登录后台
        """

        # Click text=系统设置
        page.click("text=系统设置")
        # Click text=站点配置
        page.click("text=站点配置")
        # Click text=权限控制
        page.click("text=权限控制")
        # Click text=用户管理
        page.click("text=用户管理")
        # Click text=商品管理
        page.click("text=商品管理")

        assert 1 == 1

if __name__ == '__main__':
    pytest.main(["-v", "-s"])



