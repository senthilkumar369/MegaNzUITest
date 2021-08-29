from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotVisibleException, \
    ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver import common
from selenium.webdriver.support import expected_conditions as EC

import selenium

import os, json,time,re

from selenium.webdriver.support.wait import WebDriverWait

from env import ROOT_DIR
from lib import helperLocator
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


configFile = os.path.join(ROOT_DIR, "ConfigsObjects", "ObjectRepository.json")
with open(configFile) as f:
    config = json.load(f)


class FileManagerPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.webloc = helperLocator.helperLocator(self.driver)

    def is_fileManager_page(self):
        filemanager_section_title = self.webloc.find_by_xpath(config['FileManagerPage']['val_file_manager_page'])
        filemanager_section_title.text
        assert filemanager_section_title.text == "FILE MANAGER"


    def get_contextMenu(self):
        menuOptions=self.webloc.find_by_xpath(config['FileManagerPage']['context_place'])
        act = ActionChains(self.driver)
        act.context_click(menuOptions).perform()
    def select_file(self):
        clk_textFile=self.webloc.find_by_xpath(config['FileManagerPage']['clk_new_text_file'])
        clk_textFile.click()

    def add_textFileName_and_create(self,Expectedfile):
        addName=self.webloc.find_by_xpath(config['FileManagerPage']['set_filename_tbox'])
        addName.clear()
        addName.send_keys(Expectedfile)
        btn_create=self.webloc.find_by_xpath(config['FileManagerPage']['btn_file_create'])
        btn_create.click()



    def write_text_and_save(self,expectedTextArea):
        import time,random
        textarea_focus=self.webloc.find_by_xpath(config['FileManagerPage']['textarea'])
        textarea_focus.click()
        codeLine = self.driver.find_element_by_css_selector("span[role='presentation']")
        act = ActionChains(self.driver)
        act.click(codeLine).perform()
        act.send_keys(expectedTextArea).perform()
        saveTest=self.webloc.find_by_xpath(config['FileManagerPage']['save_text_area']) # Save TEXT AREA
        saveTest.click()
        close_cross_button=self.webloc.find_by_xpath(config['FileManagerPage']['close_textArea'])
        time.sleep(5)
        close_cross_button.click()


    # def confirm_file_created(self,expectedfilename):
    #     confirm=self.webloc.find_by_xpath(config['FileManagerPage']['confirm_file_on_fm'])
    #     ACTUAL_FILENAME=confirm.text
    #     if not ACTUAL_FILENAME is 'expectedfilename':
    #         raise AssertionError("Incorrect File Name,actual filename %s - Expected file name %s",ACTUAL_FILENAME,expectedfilename)



    def delete_expected_file(self,Expected_filename):
        """
       @  find expected file and right click (context menu) using action chain
       @  click remove option from the context menu
       @  click confirm to remove file
        """

        element=self.lookup_a_file(Expected_filename)
        self.open_context_menu_and_delete_file(element)

    def delete_a_file_from_table_file_manager(self,Expected_filename):
        """
              @  find expected file and right click (context menu) using action chain
              @  click remove option from the context menu
              @  click confirm to remove file
               """
        self.webloc.find_by_xpath(config['FileManagerPage']['filemanager_commonarea']).click()
        elements = self.driver.find_elements_by_xpath(config['FileManagerPage']['Table_in_file_manager'])
        act = ActionChains(self.driver)
        for e in elements:
            # print("eTEXT %s ::::: expected %s"%(e.text,Expected_filename))
            if str(Expected_filename) in e.text:
                print("table value is", e.text)
                act.click(e).perform()
                act.context_click(e).perform()
                self.webloc.find_by_xpath(config['FileManagerPage']['Option_remove_in_contextmenu']).click()
                self.webloc.find_by_xpath(config['FileManagerPage']['confirm_remove_file']).click()





    def confirm_file_not_exist(self,Expected_filename):
        #self.webloc.find_by_xpath(config['FileManagerPage']['Table_in_file_manager']).click()
        #elements = self.driver.find_elements_by_xpath(config['FileManagerPage']['Table_in_file_manager'])
        self.driver.refresh()

        if Expected_filename in self.driver.page_source:
            raise AssertionError("FILE STILL EXIST, Not Deleted - FileName %s"%Expected_filename)

    def confirm_file_exist(self,Expected_filename):
        print("expected file is 5s",Expected_filename)
        if not Expected_filename in self.driver.page_source:
            raise AssertionError("FILE not EXIST,  - FileName %s"%Expected_filename)

    def goto_rubbish_bin_page(self):
        rubbish_bin_sidebar = self.webloc.find_by_xpath(config['FileManagerPage']['rubbish_bin_link_sidebar'])
        rubbish_bin_sidebar.click()




