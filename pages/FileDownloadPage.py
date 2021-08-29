from selenium import webdriver
import os, json,time
from env import ROOT_DIR
from lib import helperLocator
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from os import walk

configFile = os.path.join(ROOT_DIR, "ConfigsObjects", "ObjectRepository.json")
with open(configFile) as f:
    config = json.load(f)

class FileDownloadPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.webloc = helperLocator.helperLocator(self.driver)

    def goto_sync_page(self):
        self.webloc.find_by_xpath(config['FileDownloadPage']['menu_platform']).click()
        #self.driver.execute_script("window.scrollBy(0,950)")
        time.sleep(10)
        self.webloc.find_by_xpath(config['FileDownloadPage']['lnk_desktop_app']).click()
        time.sleep(10)

        self.driver.execute_script("window.scrollTo(0, 700)")
        link = self.driver.find_element_by_tag_name("html")
        link.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        link.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)


        #self.driver.execute_script("window.scrollBy(0,450)")
        time.sleep(4)
        self.webloc.find_by_xpath(config['FileDownloadPage']['option_linux_tab']).click()



    def check_if_download_inprogress(self):

        for (dirpath, dirnames, filenames) in walk("c:/Users/senthilk/Downloads/"):
            return str(filenames)

    def wait_for_files_to_download(self):
        time.sleep(5)  # let the driver start downloading
        file_list = self.check_if_download_inprogress()
        while 'Unconfirmed' in file_list or 'crdownload' in file_list:
            file_list = self.check_if_download_inprogress()
            time.sleep(1)


    def get_filename_from_download_link(self):
        from urllib.parse import urlparse
        self.download=self.webloc.find_by_xpath(config['FileDownloadPage']['btn_download'])
        downloadlnk = urlparse(self.download.get_attribute('data-link'))
        actual_download_file_name = downloadlnk.path.partition('64/')[2]
        return actual_download_file_name


    def validate_file_exist(self,actual_download_file_name):
        count=0
        while True:
            if os.path.exists("c:/Users/senthilk/Downloads/" + str(actual_download_file_name)):
                print("File exist", "c:/Users/senthilk/Downloads/" + str(actual_download_file_name))
                break
            if count>20:
                return TimeoutError
            count=count+1
            time.sleep(1)


    def Linux_app_select_and_download(self):

        self.dropDown=self.webloc.find_by_xpath(config['FileDownloadPage']['dropdown_control']) # click drop down
        self.dropDown.click()
        get_webElements_list= self.driver.find_elements_by_xpath(config['FileDownloadPage']['list_locator'])
        count = 1
        for e in get_webElements_list:
            print(e.text)
            e.click()
            if count == get_webElements_list:
                break
            actual_download_file_name=self.get_filename_from_download_link()
            self.download.click()
            self.wait_for_files_to_download()
            self.validate_file_exist(actual_download_file_name)
            self.dropDown.click()
            print("count", count)
            count = count + 1