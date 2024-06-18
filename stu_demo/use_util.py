from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



def get_element(driver,*loc):
    e = driver.find_element(*loc)
    return e


if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    sleep(2)
    loc = (By.ID,'kw')
    loc2 = (By.ID,'su')
    get_element(driver,*loc).send_keys('python')        #加*表示参数需要解包
    sleep(2)
    get_element(driver,*loc2).click()
    sleep(10)