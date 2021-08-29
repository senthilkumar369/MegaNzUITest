from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
import ConfigsObjects
import os,json,time
from env import ROOT_DIR
from pages import FileManagerPage
from lib import helperLocator

configFile = os.path.join(ROOT_DIR, "ConfigsObjects", "ObjectRepository.json")
with open(configFile) as f:
    config = json.load(f)

class LoginPage(object):

    def __init__(self,driver):
        self.driver=driver
        self.webloc = helperLocator.helperLocator(self.driver)

    def is_page_correct(self):
        HOME_Title="Login - MEGA"
        print("page tile ",self.driver.title)
        assert HOME_Title in self.driver.title

    def loginWithValidUserNameAndPassword(self):
        txt_UserName=self.webloc.find_by_id(config['LoginPage']['txtbox_username'])
        txt_password=self.webloc.find_by_id(config['LoginPage']['txtbox_password'])
        lnk_login_button=self.webloc.find_by_xpath(config['LoginPage']['btn_loginlink'])
        txt_UserName.clear() # clear user name field if contains anything
        txt_password.clear()# clear password field if contains anything
        txt_UserName.send_keys(config["LoginPage"]["username_id"])
        txt_password.send_keys(config["LoginPage"]["password_id"])
        lnk_login_button.click()
        time.sleep(4)
        return FileManagerPage.FileManagerPage(self.driver)
