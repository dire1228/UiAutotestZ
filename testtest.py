# -*- coding: utf-8 -*-

from selenium import webdriver
import pytest

@pytest.fixture()
def fixture_prepare():
    print("执行前操作")

def test_01(fixture_prepare):
    print("测试中")

if __name__ == '__main__':
    # selenium测试
    driver = webdriver.Chrome()
    driver.get("https://mgt.oilchem.net/login/login.htm")

    # pytest测试
    pytest.main(['-s', 'testtest.py'])
