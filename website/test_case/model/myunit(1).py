from drivers.driver import *
import unittest

"""
用例执行前后准备工作
"""

class StartEnd(unittest.TestCase):

    def setUp(self):
        """
        浏览器初始
        """
        self.driver = statrDriver()
        #设置隐式等待
        self.driver.implicitly_wait(10)
        #设置窗口最大化
        self.driver.maximize_window()

    def tearDown(self):
        """
        浏览器关闭
        """
        self.driver.quit()