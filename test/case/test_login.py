# -*- coding: utf-8 -*-
import pytest

from test.pages.loginPage import LoginPage


class TestLogin:

    @pytest.fixture()
    def fixture_yield(self):
        self.login = LoginPage()
        yield
        self.login.quit_driver()

    def test_login(self):
        """登录测试"""
        self.login.login()

if __name__ == '__main__':
    pytest.main(['-s', '--setup-show', 'test_login.py'])