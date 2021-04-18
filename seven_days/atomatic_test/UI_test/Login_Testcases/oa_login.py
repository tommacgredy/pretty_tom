from atomatic_test.UI_test.Login_Testcases.myunit import *


logging.basicConfig(format="[%(asctime)s] [%(levelname)s] %(message)s",level=logging.INFO)

class Login(TestWebUI):


    def test01_login_usrname_error(self):
        url = "http://192.168.0.8:8080/oa/login.jsp"
        self.browser.get(url)
        sleep(2)
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[1]/td[2]/input').clear()
        sleep(1)
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[1]/td[2]/input').send_keys("fux")
        logging.info("=====输入用户名=====")
        sleep(2)
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[2]/td[2]/input').clear()
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[2]/td[2]/input').send_keys("f1234567")
        logging.info("=====输入密码=====")
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="button_submit"]').click()
        logging.info("=====点击登录=====")
        sleep(2)
        create_text_02 = self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]').text
        logging.info("-----" + create_text_02 + "-----")
        self.assertIn("登录名或密码错误", create_text_02, "登录失败")

    def test02_login_passwd_error(self):
        url = "http://192.168.0.8:8080/oa/login.jsp"
        self.browser.get(url)
        sleep(2)
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[1]/td[2]/input').clear()
        sleep(1)
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[1]/td[2]/input').send_keys("fuc")
        logging.info("=====输入用户名=====")
        sleep(2)
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[2]/td[2]/input').clear()
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[2]/td[2]/input').send_keys("f12345678")
        logging.info("=====输入密码=====")
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="button_submit"]').click()
        logging.info("=====点击登录=====")
        sleep(2)
        create_text_02 = self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td/div/table/tbody/tr/td[2]').text
        logging.info("-----" + create_text_02 + "-----")
        self.assertIn("登录名或密码错误", create_text_02, "登录失败")

    def test03_login_success(self):
        url = "http://192.168.0.8:8080/oa/login.jsp"
        self.browser.get(url)
        sleep(2)
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[1]/td[2]/input').clear()
        sleep(1)
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[1]/td[2]/input').send_keys("fuc")
        logging.info("=====输入用户名=====")
        sleep(2)
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[2]/td[2]/input').clear()
        self.browser.find_element_by_xpath(
            '//*[@id="loginDiv"]/div[5]/form/div/div[2]/table/tbody/tr[2]/td[2]/input').send_keys("f1234567")
        logging.info("=====输入密码=====")
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="button_submit"]').click()
        logging.info("=====点击登录=====")
        sleep(2)
        logging.info("=====登录成功=====")
        create_text_01 = self.browser.current_url
        logging.info("-----"+create_text_01+"-----")
        self.assertEqual(create_text_01, "http://192.168.0.8:8080/oa/index.jsp", "页面跳转失败")


