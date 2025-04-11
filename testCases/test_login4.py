import time

from selenium import webdriver
from PageObject.LoginPage import LoginPage


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    useremail = "admin@yourstore.com"
    password = "admin"

    def test_homePagetitle(self, setup):
        self.diver = setup
        self.diver.get(self.baseURL)
        act_title = self.diver.title

        if act_title == "nopCommerce demo store. Login":
            assert True
            self.diver.close()
        else:
            self.diver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.diver.close()
            assert False

    def test_login(self, setup):
        self.diver = setup
        self.diver.get(self.baseURL)

        self.lp = LoginPage(self.diver)
        self.lp.setUserEmail(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(10)

        act_title = self.diver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.diver.close()
        else:
            self.diver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.diver.close()
            assert False
