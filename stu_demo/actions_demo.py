from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.get('https://sahitest.com/demo/')
    def double_click(self):
        wd = WebDriverWait(self.utils, 10)
        self.utils.find_element(By.LINK_TEXT,'Clicks Page').click()
        wd.until(EC.title_is('Clicks'))
        btn = self.utils.find_element(By.XPATH,'/html/body/form/input[2]')
        ActionChains(self.utils).double_click(btn).perform()
        sleep(2)

    def click_test(self):
        wd = WebDriverWait(self.utils, 10)
        # self.utils.find_element(By.LINK_TEXT,'Clicks Page').click()
        wd.until(EC.title_is('Clicks'))
        self.utils.find_element(By.XPATH,'/html/body/form/input[3]').click()
        # ActionChains(self.utils).click(btn).perform()
        sleep(2)

    def context_click_test(self):
        wd = WebDriverWait(self.utils, 10)
        wd.until(EC.title_is('Clicks'))
        btn = self.utils.find_element(By.XPATH,'/html/body/form/input[4]')
        ActionChains(self.utils).context_click(btn).perform()

    def atciom_test(self):
        wd = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.LINK_TEXT,'Clicks Page').click()
        wd.until(EC.title_is('Clicks'))

        # 每次ActionChains(self.utils)都会实例化一个对象，导致最后无法运行
        # ActionChains(self.utils).double_click(self.utils.find_element(By.XPATH,'/html/body/form/input[2]')).pause(1)
        # ActionChains(self.utils).click( self.utils.find_element(By.XPATH,'/html/body/form/input[3]')).pause(1)
        # ActionChains(self.utils).context_click(self.utils.find_element(By.XPATH, '/html/body/form/input[4]')).pause(1)
        # ActionChains(self.utils).perform()
        #
        #



        act1 = ActionChains(self.driver).double_click(self.driver.find_element(By.XPATH,'/html/body/form/input[2]'))
        act2 = ActionChains(self.driver).click( self.driver.find_element(By.XPATH,'/html/body/form/input[3]'))
        act3 = ActionChains(self.driver).context_click(self.driver.find_element(By.XPATH, '/html/body/form/input[4]'))
        act_list = [act1, act2, act3]
        for act in act_list:
            act.perform()
        # 同一种写法
        # ac = ActionChains(self.utils)
        # ac.double_click(self.utils.find_element(By.XPATH,'/html/body/form/input[2]'))
        # ac.click( self.utils.find_element(By.XPATH,'/html/body/form/input[3]'))
        # ac.context_click(self.utils.find_element(By.XPATH, '/html/body/form/input[4]'))
        # ac.perform()

        text = self.driver.find_element(By.XPATH,'/html/body/form/textarea').get_attribute('value')
        print('文本内容是：'+text)
        sleep(2)

    # def atciom_test2(self):
    #     wd = WebDriverWait(self.utils, 10)
    #     self.utils.find_element(By.LINK_TEXT,'Clicks Page').click()
    #     wd.until(EC.title_is('Clicks'))
    #     ActionChains(self.utils).double_click(self.utils.find_element(By.XPATH,'/html/body/form/input[2]')).perform()
    #     sleep(2)
    #     ActionChains(self.utils).click( self.utils.find_element(By.XPATH,'/html/body/form/input[3]')).perform()
    #     sleep(2)
    #     ActionChains(self.utils).context_click(self.utils.find_element(By.XPATH, '/html/body/form/input[4]')).perform()
    #     text = self.utils.find_element(By.XPATH,'/html/body/form/textarea').get_attribute('value')
    #     print('文本内容是：'+text)
    #     sleep(2)







if __name__ == '__main__':
    test = TestCase()
    # test.double_click()
    # test.click_test()
    # test.context_click_test()
    test.atciom_test()