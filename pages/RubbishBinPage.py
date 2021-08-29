from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
import ConfigsObjects
import os,json,time
from env import ROOT_DIR
from lib import helperLocator
from selenium.webdriver import ActionChains
from pages import FileManagerPage
configFile = os.path.join(ROOT_DIR, "ConfigsObjects", "ObjectRepository.json")
with open(configFile) as f:
    config = json.load(f)

class RubbishBinPage(object):
    def __init__(self,driver):
        self.driver=driver
        self.webloc = helperLocator.helperLocator(self.driver)

    def find_and_restore_files(self,filename):
        # tablefr = self.webloc.find_by_xpath(config['RubbishBinPage']['binfileslist'])
        # tablefr.click()
        # elements = self.webloc.find_all_elements_by_tag('tr')
        self.webloc.find_by_xpath(config['RubbishBinPage']['Rubbish_commonarea']).click()
        elements = self.driver.find_elements_by_xpath(config['RubbishBinPage']['Table_in_Rubbish_tab'])
        for e in elements:
            if filename in e.text:
                print(e.text)
                e.click()
                time.sleep(2)
                act = ActionChains(self.driver)
                act.context_click(e).perform()
                time.sleep(3)
                self.webloc.find_by_xpath(config['RubbishBinPage']['lnk_restore']).click()

    def goto_clouddrive(self,):
        """
               @   To find a file, get list ,search
               @   if exist then throw assertion error
               """
        cloudDrivesideBar_Link=self.driver.find_element_by_xpath(config['RubbishBinPage']['cloudDrive_link_sideBar'])
        cloudDrivesideBar_Link.click()



