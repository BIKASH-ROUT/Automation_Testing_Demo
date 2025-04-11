import time

import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    useremail = "admin@yourstore.com"
    password = "admin"

    def test_homePagetitle(self):
        self.diver = webdriver.Chrome()
        self.diver.get(self.baseURL)
        act_title = self.diver.title
        self.diver.close()

        if act_title == "nopCommerce demo store. Login":
            assert True
        else:
            assert False

    def test_login(self):
        self.diver = webdriver.Chrome()
        self.diver.get(self.baseURL)

        self.lp = LoginPage(self.diver)
        self.lp.setUserEmail(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.diver.title
        time.sleep(10)
        self.diver.close()

        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
