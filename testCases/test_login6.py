import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from Utilities import readProperties
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePagetitle(self, setup):
        self.logger.info("******** Test_001_Login ********")
        self.logger.info("******** Verifying Home Page Title ******")
        self.diver = setup
        self.diver.get(self.baseURL)
        act_title = self.diver.title

        if act_title == "nopCommerce demo store. Login":
            assert True
            self.logger.info("********* Home Page Title test is passed *********")
            self.diver.close()

        else:
            self.diver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.logger.error("******** Home page Title test is failed ********")
            self.diver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("******** Verifying Login Test ********")
        self.diver = setup
        self.diver.get(self.baseURL)

        self.lp = LoginPage(self.diver)
        self.lp.setUserEmail(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.diver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.diver.close()
            self.logger.info("******** Login test is passed ********")

        else:
            self.diver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.diver.close()
            self.logger.error("******** Login test is failed ********")
            assert False
