# -*- coding: utf-8 -*-
import os

from selenium.webdriver.common.by import By

from test.pages.basePage import BasePage
from utils.readConfig import ReadConfig


class LoginPage(BasePage):
    """登录页面"""
    def user_name_element(self):
        """用户名"""
        return self.find_element(By.ID, "name")

    def password_element(self):
        """密码"""
        return self.find_element(By.ID, "password")

    def login_element(self):
        """登录按钮"""
        return self.find_element(By.CLASS_NAME, "four")

    def login(self, username=None, password=None):
        """登录操作"""
        BasePage.open_page(self)
        username_json, password_json = self.get_account()
        if username is None:
            username = username_json
        else:
            username = username
        if  password is None:
            password = password_json
        else:
            password = password
        self.user_name_element().send_keys(username)
        self.password_element().send_keys(password)
        self.login_element().click()


    def get_account(self):
        """获得默认的账号密码"""
        current_path = os.path.abspath(os.path.dirname(__file__))
        json_path = current_path + '/../../config/base_data.json'
        account = ReadConfig().read_json(json_path)
        return account['user_name'], account['password']