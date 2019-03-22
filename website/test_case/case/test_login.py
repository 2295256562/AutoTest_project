import unittest
from website.test_case.model import function, myunit
from website.test_case.page_object.LoginPage import *
from time import sleep


# 登录用例设计
class LoginTest(myunit.StartEnd):
    def test_login_normal(self):
        """用户名密码正确"""
        print("test_login1_normal is start test... ")
        po = loginPage(self.driver)
        po.Login_action('', '')  # 调用登录方法
        sleep(2)
        # 判断两个值是否相等
        self.assertEqual()
        # 截图,传入两个参数第一个driver，第二个截图名称
        function.insert_img(self.driver, '')
