from selenium import webdriver

def statrDriver():
    """
    启动浏览器模块
    :return:
    """
    driver = webdriver.Firefox()
    return driver

if __name__ == '__main__':
    statrDriver()