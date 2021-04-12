from common.tools import Tools
from playwright.async_api import Page

class BaiduSearchPage:

    def __init__(self, page: Page):
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
        self.page.goto(self.url)

    def search_keywords(self, keywords: str):
        self.page.type(self.search_input, text=keywords)
        self.page.click(self.search_button)
