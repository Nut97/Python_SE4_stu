from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestCast(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
    def test(self):
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        sleep(1)
        self.driver.find_element(By.ID,'su').click()
        sleep(2)
        # self.utils.quit()
    def name_test2(self):
        #By.NAME可能返回多个元素，查找时会选择第一个
        self.driver.find_element(By.NAME,'wd').send_keys('selenium')
        # self.utils.find_elements(By.NAME,'wd')  返回一个集合
        sleep(2)
        self.driver.find_element(By.ID,'su').click()
        sleep(5)
        self.driver.quit()

    def link_test3(self):
        self.test()
        self.driver.find_element(By.LINK_TEXT,'百度首页').click()
        sleep(5)
    def link_partial_test(self):
        self.test()
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'百度').click()
        sleep(5)

    def xpath_test(self):
        self.test()
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('极客时间')
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()
        sleep(2)

    def tag_test(self):
        self.test()
        input = self.driver.find_element(By.TAG_NAME,'input')
        print(input)

    def css_selector_test(self):
        self.test()
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('极客时间')
        self.driver.find_element(By.CSS_SELECTOR,'#su').click()

    def class_name_test(self):
        self.test()
        self.driver.find_element(By.CLASS_NAME,'s_ipt').send_keys('极客时间')
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()

    def test_all(self):
        self.driver.find_element(value='kw').send_keys('极客时间')
        self.driver.find_element(value='su').click()
        sleep(2)
    def exit_test(self):
        input("Press any key to exit...")

if __name__=='__main__':
    case = TestCast()
    case.test_all()
    case.exit_test()