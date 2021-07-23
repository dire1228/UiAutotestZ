# -*- coding: utf-8 -*-
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logConfig import Log

log = Log().get_log()


class BasePage(object):
    """基础页面"""
    # 记录对象是否被创建
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, driver=None, base_url=None):
        """
        基础的参数，webdriver、默认访问的url
        :param driver: 浏览器驱动
        :param base_url: 默认打开的url，一般都是登录页面
        """
        print(1111)
        # # 浏览器设置
        # options = webdriver.ChromeOptions()
        # # 屏蔽浏览器检测
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # # 禁用保存密码弹窗
        # prefs = {"": "", "credentials_enable_service": False, "profile.password_manager_enabled": False}
        # options.add_experimental_option("prefs", prefs)
        # # 设置浏览器编码
        # options.add_argument("lang=zh_CN.UTF-8")
        # log.debug("prefs" + str(options))
        if driver is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            self.driver_path = current_path + '/../../drivers/chromedriver.exe'
            # self.driver = webdriver.Chrome(driver_path, options=options)
        else:
            self.driver = driver
        if base_url is None:
            self.base_url = "https://mgt.oilchem.net/login/login.htm"
        else:
            self.base_url = base_url

    def init_webdriver(self):
        # 浏览器设置
        options = webdriver.ChromeOptions()
        # 屏蔽浏览器检测
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 禁用保存密码弹窗
        prefs = {"": "", "credentials_enable_service": False, "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        # 设置浏览器编码
        options.add_argument("lang=zh_CN.UTF-8")
        log.debug("prefs" + str(options))
        self.driver = webdriver.Chrome(self.driver_path, options=options)

    def open_page(self):
        """打开默认页面"""
        self.init_webdriver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        sleep(1)

    def close_page(self):
        """关闭页面"""
        return self.driver.close()

    def quit_driver(self):
        """关闭页面并退出程序"""
        return self.driver.quit()

    def find_element(self, by, element):
        """返回单个定位元素"""
        sleep(1)
        return self.driver.find_element(by, element)

    def find_elements(self, by, element):
        """返回一组元素"""
        sleep(1)
        return self.driver.find_elements(by, element)

    def switch_alert(self):
        """返回弹窗界面"""
        sleep(1)
        return self.driver.switch_to.alert

    def select_menu(self, menu_text):
        """菜单选择"""
        sleep(1)
        menus_element = self.driver.find_elements(By.CSS_SELECTOR, "#menu>div>h4")
        for menu in menus_element:
            # replace(" ", "")去掉字符串中的空格
            if menu.text.replace(" ", "") == menu_text.replace(" ", ""):
                return menu.click()
        print(menu_text + "未找到")
        return

    def log_out(self):
        """退出登录"""
        return self.select_menu("退出登录")
