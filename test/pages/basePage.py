# -*- coding: utf-8 -*-
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logConfig import Log

log = Log("BasePage").get_log()


class BasePage(object):
    """基础页面"""
    # 记录对象是否被创建
    instance = None
    # 记录是否执行初始化操作
    init_flag = False
    # 记录log是否初始化
    log_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否为空对象，若为空说明第一个对象还没被创建
        if cls.instance is None:
            # 2.对第一个对象没有被创建，我们应该调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 3.把类属性中保存的对象引用返回给python的解释器
        return cls.instance

    def __init__(self, base_url=None):
        """
        基础的参数，webdriver、默认访问的url
        :param driver: 浏览器驱动
        :param base_url: 默认打开的url，一般都是登录页面
        """
        log.info("执行BasePage构造方法")
        # 只有driver没有初始化的时候才会初始化driver
        if BasePage.init_flag:
            log.debug("true driverFlag：" + str(self.driverFlag))
        else:
            current_path = os.path.abspath(os.path.dirname(__file__))
            self.driver_path = current_path + '/../../drivers/chromedriver.exe'
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
            self.driverFlag = True
            log.debug("false driverFlag：" + str(self.driverFlag))
            log.debug("初始化driver完毕：" + str(self.driver))

        if base_url is None:
            self.base_url = "https://mgt.oilchem.net/login/login.htm"
        else:
            self.base_url = base_url

    def open_page(self):
        """打开默认页面"""
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


if __name__ == '__main__':
    bp = BasePage()
    bp.open_page()
