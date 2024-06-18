from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service

service  = Service('../utils/chromedriver.exe')
class IframeDemo(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('https://www.sahitest.com')
        self.driver.maximize_window()

    def iframe_test(self):
        self.driver.find_element(By.LINK_TEXT,'demo').click()
        self.driver.find_element(By.LINK_TEXT,'Frames Test').click()
        top= self.driver.find_element(By.NAME,'top')                            #切换到iframe框架
        self.driver.switch_to.frame(top)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Form Test').click()
        alert = self.driver.switch_to.alert
        alert.accept()
        sleep(2)
        self.driver.switch_to.default_content()
        second = self.driver.find_element(By.XPATH,'/html/frameset/frame[2]')
        self.driver.switch_to.frame(second)
        self.driver.find_element(By.LINK_TEXT,'IFrame via doc write').click()
        sleep(2)
        self.driver.back()
        sleep(2)


if __name__ == '__main__':
    I = IframeDemo()
    I.iframe_test()
    sleep(2)