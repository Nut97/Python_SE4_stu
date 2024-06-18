import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class   TestCase(object):
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://www.baidu.com")

    def test_sleep(self):
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        sleep(2)
        self.driver.find_element(By.ID,'su').click()
        sleep(2)

    def test_implicitly_wait(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID,'su').click()
        sleep(2)

    def test_WebDriverWait(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_is('百度一下，你就知道'))
        self.driver.find_element(By.ID,'kw').send_keys('selenium')

        self.driver.find_element(By.ID,'su').click()
        sleep(2)

class TestCase2(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path +'/time_out.html'
        self.driver.get(file_path)

    def test2(self):

        self.driver.find_element(By.ID,'btn').click()
        #显示等待
        wd = WebDriverWait(self.driver, 3)
        wd.until(EC.text_to_be_present_in_element((By.ID,'id2'),'id 2'))            #EC通过EC判断+显示等待使等待元素出现后进行下一步
        print(self.driver.find_element(By.ID, 'id2').text)
        print("ok")
        sleep(4)

if __name__ == '__main__':
    test = TestCase()
    test.test_WebDriverWait()