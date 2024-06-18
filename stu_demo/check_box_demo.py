import os.path

from selenium import   webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

class From_box(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/form_box.html'
        self.driver.get(file_path)
        sleep(3)
    def test_checkbox(self):
        swiming= self.driver.find_element(By.NAME, 'checkbox')
        if not swiming.is_selected():
            swiming.click()
        reading = self.driver.find_element(By.NAME, 'reading')
        if not reading.is_selected():
            reading.click()
        sleep(3)
        swiming.click()
        sleep(5)

    def test_radio(self):
        list = self.driver.find_elements(By.NAME, 'genner')
        list[0].click()
        sleep(5)



if __name__ == '__main__':
    case = From_box()
    case.test_radio()