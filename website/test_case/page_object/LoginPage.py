from selenium import webdriver

#登录页面
from selenium.webdriver.common.by import By
from website.test_case.page_object.BasePage import Page


class loginPage(Page):

    url = ''
    password_loc = ()
    username_loc = ()
    submit_loc = ()


    def type_username(self,username):
        """
        用户名输入封装
        :param username:
        :return:
        """
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        """
        密码输入封装
        :param password:
        :return:
        """
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        """
        点击事件封装
        :return:
        """
        self.find_element(*self.submit_loc).click()

    def Login_action(self,username,password):
        """
        登录方法
        :param username:
        :param password:
        :return:
        """
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()


    loginPass_loc = (By.LINK_TEXT,'')  #登录成功后定位页面是否有这个元素
    logFail_loc = (By.NAME,'')         #登录失败定位输入用户名或密码元素

    def type_loginPass(self):
        #获取到登录成功后元素的对应值
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail(self):
        return self.find_element(*self.logFail_loc).text
