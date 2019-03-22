import unittest

import time

from website.test_case.model.function import *


report_dir = './test_report'
test_dir = './test_case'

print("启动case")
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
now = time.strftime("%Y-%m-%d:%H_%M_%S")
report_name = report_dir+'/'+now+'result.html'

print("start write report...")
with open(report_name,'wb') as f:
    runner = BSTestRunner(stream=f,title="Test Report", description="login test")
    runner.run(discover)
    f.close()

print("find lattest report")
latest_report = latest_report(report_dir)

print("send email report")
send_mail(latest_report)

print("Test end")
