"""
@author:  wangquaxiu
@time:  2019/3/19 21:17
"""
import os
import time
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome import options
from selenium.common.exceptions import InvalidArgumentException


class ReuseChrome(Remote):

    def __init__(self, command_executor, session_id):
        self.r_session_id = session_id
        Remote.__init__(self, command_executor=command_executor, desired_capabilities={})

    def start_session(self, capabilities, browser_profile=None):
        """
        重写start_session方法
        """
        if not isinstance(capabilities, dict):
            raise InvalidArgumentException("Capabilities must be a dictionary")
        if browser_profile:
            if "moz:firefoxOptions" in capabilities:
                capabilities["moz:firefoxOptions"]["profile"] = browser_profile.encoded
            else:
                capabilities.update({'firefox_profile': browser_profile.encoded})

        self.capabilities = options.Options().to_capabilities()
        self.session_id = self.r_session_id
        self.w3c = False

# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver


# browser = webdriver.Chrome(executable_path = os.path.abspath(r'C:\Users\wangq\AppData\Local\Google\Chrome\Application\chromedriver.exe'))

browser = openChrome()
executor_url = browser.command_executor._url
session_id = browser.session_id

browser.get('http://sns.qnzs.youth.cn/question/ask/')

print("测试。。。。")
time.sleep(20)
print("延时结束")

# 使用ReuseChrome()复用上次的session
driver2 = ReuseChrome(command_executor=executor_url, session_id=session_id)

with open('G:\学习资料\党课\问题答案.txt','r') as file:
    for line in file.readlines():

        # browser.get('http://sns.qnzs.youth.cn/index/newlist')


        print(line)
        browser.get('http://sns.qnzs.youth.cn/question/ask/')
        input_title = browser.find_element_by_id('user-ask-title')
        input_title.send_keys(line)
        browser.find_element_by_class_name("user-ask-btn").click()
        print('提问加一。。')
        time.sleep(600)