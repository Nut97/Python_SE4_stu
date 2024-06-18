import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select                #下拉框选项的模块


class Xiala(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/xiala.html'
        self.driver.get(file_path)
        sleep(2)

    def test_select(self):                                          #下拉选择select类
        se = self.driver.find_element(By.ID,'provide')
        select = Select(se)
        # select.select_by_index(0)
        # sleep(2)
        # select.select_by_visible_text('Tianjing')
        # sleep(2)
        # select.select_by_value('sh')
        # sleep(2)
        # for i in range(3):
        #     select.select_by_index(i)                               #选择元素
        #     sleep(1)
        # sleep(2)
        # select.deselect_all()                                       #全部反选
        # sleep(2)

        for option in select.options :
            print(option.text)



if __name__ == '__main__':
    case = Xiala()
    case.test_select()
