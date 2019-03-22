from selenium import webdriver
import os

# 截图
def insert_img(driver,filename):
    func_path = os.path.dirname(__file__)
    print(func_path)

    base_dir = os.path.dirname(func_path)
    print(base_dir)

    base_dir =str(base_dir)
    #\\转义为/
    base_dir = base_dir.replace('\\', '/')
    print(base_dir)

    base = base_dir.split('/website')[0]
    print(base)

    filepath = base+'/website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(filepath)

# 发送邮件


# 查找最新报告

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.sogou.com')
    insert_img(driver,'sougou.png')
    driver.quit()