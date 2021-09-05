import os
import time
import pytest

now_time=time.strftime("%Y_%m_%d_%H_%M_%S")
print(now_time)
current_path=os.path.dirname(__file__)

json_report=os.path.join(current_path,'report/json',now_time)
html_report=os.path.join(current_path,'report/html',now_time)

os.mkdir(json_report)
os.mkdir(html_report)


pytest.main(['--alluredir=%s'%json_report,'-v','-s'])
os.system('allure generate %s -o %s'%(json_report,html_report))
