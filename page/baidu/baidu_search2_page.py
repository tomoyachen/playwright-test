from common.tools import Tools
from playwright.async_api import Page

# 利用 global 简化 page使用
page: Page

class BaiduSearchPage:

    def __init__(self, page_: Page):
        global page
        page = page_

        self.page = page
        self.host = Tools.get_config("base_url")
        self.path = "/"
        self.url = self.host + self.path
        self.search_input = "#kw"  # 搜索框
        self.search_button = "#su"  # 搜索按钮
        self.settings = "#s-usersetting-top"  # 设置
        self.search_setting = "#s-user-setting-menu > div > a.setpref"  # 搜索设置
        self.save_setting = 'text="保存设置"'  # 保存设置

    def open(self):
        page.goto(self.url)

    def search_keywords(self, keywords: str):
        page.type(self.search_input, text=keywords)
        page.click(self.search_button)
