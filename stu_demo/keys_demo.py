from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCase(object):
    def __init__(self, driver):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def keys_test(self):
        self.driver.get("https://www.baidu.com")
        kw = self.driver.find_element(By.ID, "kw")
        su = self.driver.find_element(By.ID, "su")
        # kw.send_keys("seleniumn")
        # kw.send_keys(Keys.CONTROL, "a")
        # sleep(2)
        # kw.send_keys(Keys.CONTROL, "x")
        # sleep(2)
        # kw.send_keys(Keys.CONTROL, "v")
        # sleep(2)
        e = self.driver.find_element(By.LINK_TEXT,'新闻')
        print(e)
        ActionChains(self.driver).move_to_element(e).perform()
        sleep(2)

if __name__ == '__main__':
    case = TestCase(webdriver)
    case.keys_test()

