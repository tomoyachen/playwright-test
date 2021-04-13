import pytest
from playwright.async_api import Page, Browser

# 我希望一个测试类里只使用一个浏览器
# 因为 pytest-playwright 内置的 browser fixture作用域是 session
# 所有 自定义 class 作用域的 page fixture 可以引入 browser fixture，并且覆盖原有的 page fixture

class AdminLoginTest:

    # scope = class, autouse = true，等同于 setup_class()
    @pytest.fixture(scope="class", autouse=True)
    def page(self, browser: Browser):

        # page 也可以放到 conftest作为全局fixture来使用
        # 注意，自己new_page会导致 browser_context_args 钩子失效，
        # 需要在 new_page() 时传入 record_video_dir 参数 才能录制视频
        page = browser.new_page()

        # Go to http://localhost/shopxo/admin.php
        page.goto("http://localhost/shopxo/admin.php")

        # 常规设计模式，在 setup_class() 中访问 base_url 并且登录。
        # 这样可以单独执行任意一个 测试方法，都能顺利打开浏览器并且登录。
        # 而同时执行整个测试集也不会重复启动浏览器与登录而浪费时间。
        yield page


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



