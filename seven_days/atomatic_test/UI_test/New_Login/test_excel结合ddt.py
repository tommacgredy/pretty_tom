#coding=utf-8
import os
import time
import xlrd
import ddt,unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC   # 导入EC模块
from selenium.webdriver.support.ui import WebDriverWait  # 导入WebDriverWait模块
import logging
from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner


logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s",level=logging.INFO)

def read_data():
    book = xlrd.open_workbook('data_info.xlsx', 'r')  # 读取data_info表格中的内容
    table = book.sheet_by_index(0)   # 读取第一个sheet页
    new_row = [table.row_values(rowvalue, 0, table.ncols) for rowvalue in range(1, table.nrows)]
    return new_row

def read_xpath_data(xpath_name):
    book = xlrd.open_workbook('data_xpath.xlsx', 'r')  # 读取data_xpath表格中的内容
    table = book.sheet_by_index(0)   # 读取第一个sheet页
    for rowvalue in range(1, table.nrows):
        if table.row(rowvalue)[0].value == xpath_name:
            return table.row(rowvalue)[1].value



@ddt.ddt
class Testlogin(unittest.TestCase):
    def setUp(self) -> None:
        url = "http://192.168.0.8:8080/oa/"
        self.brower = webdriver.Firefox()
        self.brower.get(url)
        sleep(1)
        self.brower.maximize_window()
        sleep(1)

    def tearDown(self) -> None:
        self.brower.quit()

    def by_xpath(self, loc):
        """重写xpath方法"""
        by_xpath = self.brower.find_element_by_xpath(loc)
        return by_xpath

    def get_assert_text(self):
        """获取验证信息"""
        error_xpath = read_xpath_data('error_xpath')
        try:
            sleep(1)
            loctor = (By.XPATH, error_xpath)
            WebDriverWait(self.brower, 5, 0.5).until(EC.presence_of_element_located((loctor)))
            return self.by_xpath(error_xpath).text
        except Exception as e:
            print('元素定位报错，原因是：{}'.format(e))


    @ddt.data(*read_data())
    @ddt.unpack
    def test_oa_login(self, username, password, text):
        username_xpath = read_xpath_data('username_xpath')
        passwd_xpath = read_xpath_data('passwd_xpath')
        login_xpath = read_xpath_data('login_xpath')
        self.by_xpath(username_xpath).clear()
        sleep(1)
        self.by_xpath(username_xpath).send_keys(username)
        logging.info("=====输入用户名=====")
        sleep(2)
        self.by_xpath(passwd_xpath).clear()
        self.by_xpath(passwd_xpath).send_keys(password)
        logging.info("=====输入密码=====")
        sleep(2)
        self.by_xpath(login_xpath).click()
        logging.info("=====点击登录=====")
        sleep(2)
        self.assertEqual(self.get_assert_text(), text)
        logging.info("=====验证信息=====:" + self.get_assert_text())


if __name__ == "__main__":
    testcase_path = os.path.dirname(__file__)
    pattern = 'test_excel结合ddt.py'
    TestSuite = unittest.defaultTestLoader.discover(testcase_path, pattern)
    fp = open(os.path.join(os.path.dirname(__file__), 'Reports',
                           time.strftime('%Y_%m_%d_%H_%M_%S') + 'report.html'), 'w', encoding='utf-8')
    runner = HTMLTestRunner(stream=fp, title='excel结合ddt测试报告', description='excel结合ddt练习')
    runner.run(TestSuite)