from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https:www.baidu.com")
        self.driver.maximize_window()

    def test_webelement_prop(self):
        e = self.driver.find_element(By.ID,'t1')
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        print(e.text)
        sleep(4)

    def testwebelement_method(self):
        e = self.driver.find_element(By.ID,'t1')
        e.send_keys('hello world')
        sleep(3)
        print(e.get_attribute('type'))
        print(e.get_attribute('value'))
        print(e.get_attribute('name'))
        print(e.get_attribute('size'))
        print(e.get_attribute('id'))
        print(e.get_attribute('tag_name'))
        print(e.get_attribute('text'))
        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))
        e.clear()
        sleep(3)

    def test_windows(self):
        self.driver.find_element(By.LINK_TEXT,'新闻').click()
        windows = self.driver.window_handles                        #获取浏览器的句柄
        print(type(windows))
        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)

if __name__ == '__main__':
    t = TestCase()
    t.test_windows()
