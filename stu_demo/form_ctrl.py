import os.path
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class FormCtrl(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path='file:///'+path+'/form.html'              #file协议加载本地文件路径
        self.driver.get(file_path)
        sleep(5)

    def test_logging(self):
        username=self.driver.find_element(By.ID,'username')
        username.send_keys('admin')
        pwd = self.driver.find_element(By.ID,'pwd')
        pwd.send_keys('PASSWORD')
        sleep(2)
        print(username.get_attribute('value'))
        print(pwd.get_attribute('value'))
        sleep(2)
        self.driver.find_element(By.ID,'sub').click()
        sleep(2)
        self.driver.switch_to.alert.accept()                    #确认弹窗
        sleep(2)
        username.clear()
        pwd.clear()
        sleep(2)


if __name__ == '__main__':
    case = FormCtrl()
    case.test_logging()