# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from test.pages.basePage import BasePage
from test.pages.loginPage import LoginPage
from utils.logConfig import Log

log = Log().get_log()


class HomePage(BasePage):

    def platform_management_element(self):
        """平台管理"""
        return self.find_element(By.CLASS_NAME, "ivu-dropdown-rel")

    def control_module_element(self, module_text):
        """
        平台管理子项
        :param module_text: 用户管理系统， 用户管理系统
        :return:
        """
        control_parent = self.find_element(By.CLASS_NAME, "ivu-dropdown-menu.list")
        control_item = control_parent.find_element(By.XPATH, "div/u1/li[text()=%(module_text)]") % {"module_text",
                                                                                                    module_text}
        return control_item

    def crm(self, module_text):
        """平台资讯管理"""
        self.platform_management_element().click()
        sleep(1)
        self.control_module_element(module_text)
        log.debug("从主页进入模块：" + module_text)

if __name__ == '__main__':
    login = LoginPage()
    login.login()
    sleep(2)
    hp = HomePage()
    hp.crm("用户管理系统")
