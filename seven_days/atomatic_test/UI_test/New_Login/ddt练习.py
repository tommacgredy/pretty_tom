import logging
import ddt
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 导入WebDriverWait类
from selenium.webdriver.support import expected_conditions as EC  # 导入EC模块


logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s",level=logging.INFO)
def Data():
    return [
        ["", "f1234567", "请输入登录名！"],
        ["fuc", "", "请输入密码！"]
    ]

@ddt.ddt
class TestMuules(unittest.TestCase):

    def setUp(self) -> None:
        url = "http://192.168.0.8:8080/oa/login.jsp"
        self.browser = webdriver.Chrome()
        sleep(2)
        self.browser.maximize_window()
        sleep(1)
        self.browser.get(url)
        sleep(2)

    def tearDown(self) -> None:
        self.browser.quit()

    def by_xpath(self, loc):
        """重写xpath方法"""
        return self.browser.find_element_by_xpath(loc)

    def get_assertText(self, xpath):
        """获取验证信息"""
        try:
            sleep(1)
            locator = (By.XPATH, xpath)
            WebDriverWait(self.browser, 5, 0.5).until(EC.presence_of_element_located((locator)))
            return self.by_xpath(xpath).text
        except Exception as e:
            print("元素定位报错，原因是:{}".format(e))


    @ddt.data(*Data())
    @ddt.unpack
    def test_oa_login(self, username, password, text):
        text_xpath = '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]'
        self.by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[1]/td[2]/input').clear()
        sleep(1)
        self.by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(username)
        logging.info("=====输入用户名=====")
        sleep(2)
        self.by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[2]/td[2]/input').clear()
        self.by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[2]/td[2]/input').send_keys(password)
        logging.info("=====输入密码=====")
        sleep(2)
        self.by_xpath('//*[@id="button_submit"]').click()
        logging.info("=====点击登录=====")
        sleep(2)
        self.assertEqual(self.get_assertText(text_xpath), text)


if __name__ == "__main__":
    unittest.main()
