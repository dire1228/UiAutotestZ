# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from utils.logConfig import Log

"""判断元素是否存在"""


class ElementIsExist(object):

    def __init__(self):
        self.log = Log().get_log()

    """判断一个元素是否存在"""

    def element_is_exist(self, driver, seletor, by=By.XPATH):
        flag = True
        try:
            driver.find_element(by=by, value=seletor)
            self.log.debug("元素是否存在：" + str(flag))
            return flag
        except Exception:
            flag = False
            self.log.debug("元素是否存在：" + str(flag))
            return flag

    """判断一组元素是否存在"""

    def elements_is_exist(self, driver, seletor, by=By.XPATH):
        flag = True
        try:
            driver.find_elements(by=by, value=seletor)
            self.log.debug("元素是否存在：" + str(flag))
            return flag
        except Exception:
            flag = False
            self.log.debug("元素是否存在：" + str(flag))
            return flag


if __name__ == '__main__':
    e = ElementIsExist()
    e.element_is_exist(1, 2, 3)
