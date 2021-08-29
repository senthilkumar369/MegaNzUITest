from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
import ConfigsObjects
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class helperLocator(object):

    def __init__(self,driver):
        Timeout = 40
        poll_frequency = 1
        self._web_driver_wait = WebDriverWait(driver, Timeout,poll_frequency,ignored_exceptions = [ElementClickInterceptedException,TimeoutException])

    def find_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_id(self, id):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_by_name(self, name):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_all_elements_by_tag(self,tag):
        return self._web_driver_wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, tag)))

    def find_all_elements_by_xpath(self, tag):
        return self._web_driver_wait.until(EC.visibility_of_all_elements_located((By.XPATH, tag)))

    def Wait_for_element_clickable_by_xpath(self,xpath):
        return self._web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    def Wait_for_element_not_tobe_visible_by_xpath(self,xpath):
        return self._web_driver_wait.until(EC.invisibility_of_element_located((By.XPATH, xpath)))





