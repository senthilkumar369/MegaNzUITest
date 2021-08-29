from selenium import webdriver
#import ConfigsObjects
import os,json
from env import ROOT_DIR
from pages import LoginPage
from lib import helperLocator
#driver=webdriver.chrome()
configFile = os.path.join(ROOT_DIR, "ConfigsObjects", "ObjectRepository.json")
with open(configFile) as f:
    config = json.load(f)

class HomePage(object):

    def __init__(self,driver):
     self.driver=driver
     self.webloc = helperLocator.helperLocator(self.driver)

    def is_page_correct(self):
        HOME_Title=config["HomePage"]["HomePage_Title"]
        assert HOME_Title in self.driver.title
    def acceptAll_cookies(self):
        obj_cookie=self.webloc.find_by_xpath(config["HomePage"]["cookie_accept_all"])
        obj_cookie.click()
    def open_login_form(self):
       link_Login=self.webloc.find_by_xpath(config["HomePage"]["lnk_Login"])
       #link_Login=self.driver.find_element(By.XPATH("//*[@id='startholder']/div[2]/div/div[1]/section/div[4]/button[2]"))
       link_Login.click()
       return LoginPage.LoginPage(self.driver)




