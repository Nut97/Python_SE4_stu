import os
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

class AutoTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/test_alert.html'
        self.driver.get(file_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        sleep(3)

    def test_alert(self):
        self.driver.find_element(By.ID,'alert').click()
        #切换到alert
        alert = self.driver.switch_to.alert
        print(alert.text)
        sleep(3)
        alert.accept()
        sleep(3)

    def test_confirm(self):
        self.driver.find_element(By.ID,'confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        sleep(3)
        confirm.dismiss()
        sleep(3)
        self.driver.find_element(By.ID,'confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        sleep(3)
        confirm.accept()
        sleep(3)

    def test_prompt(self):
        self.driver.find_element(By.ID,'prompt').click()
        promp= self.driver.switch_to.alert                              # 所有弹窗切换都是switch_to.alert
        print(promp.text)
        sleep(2)
        promp.send_keys('20')
        sleep(5)
        promp.accept()
        sleep(3)

if __name__ == '__main__':
    case = AutoTest()
    case.test_prompt()
