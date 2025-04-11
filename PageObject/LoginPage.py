from selenium import webdriver
from selenium.webdriver.common.by import By

# create class object for login page
class LoginPage:
    textbox_useremail_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
# after login we also logout the account in another page
    link_logout_linktext = "Logout"

# create constructor and call local driver
    def __init__(self, driver):
        self.driver = driver

# create action methods:-
    def setUserEmail(self, useremail):
        self.driver.find_element(By.ID,self.textbox_useremail_id).clear()
        self.driver.find_element(By.ID,self.textbox_useremail_id).send_keys(useremail)

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()