from time import sleep

"""
页面基础类
"""


class Page():

    # 初始化
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.baidu.com'
        self.timeout = 10

    def _open(self, url):
        """
        打开不同的子页面
        """
        url_ = self.base_url+url
        print("打开是页面是: %s" % url_)
        #窗口最大化
        self.driver.maximze_window()
        #打开具体的url
        self.driver.get(url_)
        sleep(2)
        #是否与我预期的一致
        assert self.driver.current_url == url_ ,'Did ont land on %s' % url_

    # 具体打开的页面
    def open(self):
        self._open(self.url)

    # 元素定位方法封装
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 定位一组元素
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)