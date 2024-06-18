import os
from time import sleep, strftime, localtime, time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service('../utils/chromedriver.exe')

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('http://www.baidu.com')

    def test(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('python')
        self.driver.find_element(By.XPATH, '//*[@id="su"]').click()
        sleep(2)
        str = strftime("%Y-%m-%d-%H-%M-%S",localtime(time()))           #以时间作为截图名称
        filename = str + '.png'                                         #给文件命名
        file_path = "../screenshot_file/"+filename                      #指定文件保存位置
        print(file_path)                                                #打印文件位置
        if self.driver.save_screenshot(file_path) :                      #打印保存结果
            print('截图保存成功')
        else:
            print('截图保存失败')
        sleep(2)


    def  screenshot_demo(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.get('http://www.baidu.com')
        wait = WebDriverWait(self.driver,10)                            #设置显示等待
        self.driver.find_element(By.ID,'kw').send_keys('bilibili')
        self.driver.find_element(By.ID,'su').click()
        wait.until(EC.title_is("bilibili_百度搜索"))                                #标题判断等待
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'干杯').click()         #找到哔哩哔哩并点击进入
        wd = self.driver.window_handles                                            #获取窗口句柄
        print(wd)                                                                   #打印句柄
        self.driver.switch_to.window(self.driver.window_handles[1])                 #切换到新窗口
        wait.until(EC.title_contains("哔哩哔哩"))                                   #判断网页是否加载完毕
        self.driver.maximize_window()                                               #最大化窗口
        str = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        filename = str + '.png'
        file_path = "../screenshot_file/"+filename                                   #设置文件路径
        if self.driver.save_screenshot(file_path):
            print("保存成功,地址为：" +"//pythonProject/screenshot_file/ 下")
        else:
            print("截图保存失败")
        sleep(3)


if __name__ == '__main__':
    test = TestCase()
    test.test()
    test.screenshot_demo()


