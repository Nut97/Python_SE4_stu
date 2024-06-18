from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testcase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
    def test_prop(self):
        print(self.driver.name)
        print(self.driver.title)
        print(self.driver.current_url)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        sleep(2)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('selenium')
        self.driver.find_element(By.XPATH, '//*[@id="su"]').click()
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.forward()
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    test = Testcase()
    test.test_method()

