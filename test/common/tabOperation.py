# -*- coding: utf-8 -*-

"""
Tab切换
"""
from time import sleep
from POTest.test.common.elementIsExist import ElementIsExist

class TabOperation(object):
    def __init__(self, driver):
        self.driver = driver
    def get_all_tab(self):
        """获取所有tab"""
        sleep(1)
        # 获取所有的tab父元素。元素定位默认使用css定位
        fathers_tabs = [
            # ['.tabs1', 'a2'],
            ['/html/body/div[1]/ul', 'li[1]'],
        ]
        # 获取页面显示父节点的所有tab
        for father_tab in fathers_tabs:
            # 使用is_exist()方法判断父节点是否存在，如果父节点不存在，则查找的tab不匹配
            father_exist = ElementIsExist(self.driver).is_exist(father_tab)
            print("father_tab：", father_tab)
            # 父节点存在则进行操作
            if father_exist:
                print("节点存在:", father_tab)
                father = self.driver.find_element_by_xpath(father_tab[0])
                # father = self.driver.find_element_by_xpath("/html/body/div[1]/ul")
                tabs = father.find_elements_by_xpath(father_tab[1])
                # tabs = father.find_elements_by_xpath("li[1]/a")
                return tabs
            else:
                print("节点不存在:", father_tab)
    def switch_tab(self, tab_text):
        """
        切换tab
        tab_text需要切换到的tab内容
        """
        tabs = self.get_all_tab()
        for tab1 in tabs:
            if tab1.text == tab_text:
                tab1.click()
                return
if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/index.html")
    sleep(1)
    tab = TabOperation(driver)
    tab.switch_tab("Tab2")
    # father = driver.find_element_by_xpath("/html/body/div[1]/ul")
    # print(father)
    # ele = father.find_element_by_xpath("li[2]")
    # print(ele)
    # ele.click()


