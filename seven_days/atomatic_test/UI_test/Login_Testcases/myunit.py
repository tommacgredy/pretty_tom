# 存放测试固件
import logging
import unittest
from time import sleep
from selenium import webdriver


logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s",level=logging.INFO)

class TestWebUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome()
        logging.info("=====打开浏览器完成=====")
        cls.browser.maximize_window()
        sleep(2)
        logging.info("=====浏览器串口最大化=====")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()
        logging.info("=====浏览器关闭=====")