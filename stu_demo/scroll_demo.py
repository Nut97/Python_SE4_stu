from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class   TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()

    def test_case(self):
        self.driver.execute_script('alert("test")')

        sleep(2)
        self.driver.switch_to.alert.accept()
        sleep(2)
    def test_case2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)

    def test_case3(self):
        js = 'var q = document.getElementById("kw"); q.style.border = "10px solid pink";'
        self.driver.execute_script(js)
        sleep(2)
    def test_case4(self):
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        sleep(2)
        self.driver.find_element(By.ID,'su').click()
        sleep(2)
        # js = 'window.scrollTo(0,document.body.scrollHeight)'
        # self.utils.execute_script(js)
        self.driver.execute_script("window.scrollTo(0, 500)")

        # self.utils.execute_script("arguments[0].scrollIntoView(true);")
        sleep(3)





if __name__ == '__main__':
    case = TestCase()
    # case.test_case()
    # case.test_case2()
    # case.test_case3()
    case.test_case4()
    sleep(2)
