
# coding: utf-8

# In[ ]:

'''
created by linjinzhong
date:2019/5/1
email:lin_jin_zhong@outlook.com

实现国科大校校园网自动登录功能，后台实时每隔一分钟检测是否连网
主要解决问题：
    １．控件的隐藏属性使其不能被操作，使用js脚本设置显示状态为block
    ２．登录界面及其他控件定位使用隐式等待
    ３．点击后显示反馈的错误信息时间不定，必须使用隐式等待
    ４．联网状态查询，使用系统ping命令传递5个包判断是否返回0
    ５．日志按时间周期循环保存和删除
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from logging.handlers import TimedRotatingFileHandler
import logging
import time
import os
import re


# In[ ]:

# 日期滚动日志
log_format = '%(asctime)s--%(filename)s[Line:%(lineno)d]--%(levelname)s--%(message)s'
log_datefmt = '%Y-%m-%d, %A, %H:%M:%S'
formatter = logging.Formatter(log_format, log_datefmt)
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger()

log_handler = TimedRotatingFileHandler(filename = "/tmp/auto_connect_log", when = 'd', interval = 1, backupCount = 3)
log_handler.setFormatter(formatter)
log_handler.suffix = "%Y-%m-%d.log"
log_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")

logger.addHandler(log_handler)


# In[ ]:

URL = "http://210.77.16.21"
REMOTE_SERVER = "119.75.217.109"
USERNAME = "2016E8008661018"
PASSWORD = "xxxxxx"


# In[ ]:

def is_connected(hostname):
    # exit_code == 0，网络连通
    exit_code = os.system("ping -c 5 {}".format(hostname))
    if exit_code:
        print("Network is disconnected!")
        logger.info("Network is disconnected!")
        return False
    print("Network is connected!")
    logger.info("Network is connected!")
    return True


# In[ ]:

def insert_or_click(driver, wait, ID, value):
    """
    Purpose: 根据ID，定位控件对象，判断该ID控件对象是否可见，并执行相应插入或者点击操作
    Input: 
        driver: 浏览器驱动
        ID: 控件对象
        value: 控件要插入的值（空则为点击控件）
    Output:
        False: 未能找到控件
        control: 控件对象
    """
    try:
        control = wait.until(EC.presence_of_element_located((By.ID, ID)))
    except:
        print("Sorry, can\'t find the {}!".format(ID))
        logger.info("Sorry, can\'t find the {}!".format(ID))
        return False
    
    if not control.is_displayed():
        print("'{}' is not visible, set it visible".format(ID))
        logger.info("'{}' is not visible, set it visible".format(ID))
        driver.execute_script("document.getElementById('{}').style.display='block'".format(ID))
    if value:
        control.clear()
        control.send_keys(value)
        print("'{}' is inserted successfully!".format(ID))
        logger.info("'{}' is inserted successfully!".format(ID))
    else:
        control.click()
        print("'{}' is clicked successfully!".format(ID))
        logger.info("'{}' is clicked successfully!".format(ID))

    return True


# In[ ]:

# 登录主函数
'''
国科大校园网控件ID可以由谷歌浏览器按F12查找
用户名：username
密码：pwd
记住密码：jizhummNo/jizhummYes
自动连接：tjNoA/tjYesA
连接登录：loginLink_div
错误信息：error_span_content
下线：　toLogOut
'''
def login_main(driver, URL, IDs):
    '''
    Purpose: 实现登录国科大校园网
    Input: 
        driver: 浏览器驱动
        URL: 登录界面的URL
    Output: 
        -1: 输入有误
         0: 网页丢失或者控件ID有误
         1: 登录是否成功
    '''
    # 进入登录界面
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 2)
    except:
        print("Sorry, the web is lost!")
        logger.info("Sorry, the web is lost!")
        return 0
    
    # 处理控件，插入或者点击
    for ID in IDs.items():
        res = insert_or_click(driver, wait, ID[0], ID[1]) 
        if not res:
            return -1

    # 判断是否有错误提示
    try:
        error_info = wait.until(EC.visibility_of_element_located((By.ID, 'error_span_content')))
        if error_info.text:
            print(error_info.text)
            logger.info(error_info)
            return -1                    
    except:
        pass
        # print('无错误提示！')
        # logger.info('无错误提示！')
    
    # 判断是否登录成功
    try:
        logout = wait.until(EC.visibility_of_element_located((By.ID, 'toLogOut')))
        print("Logging Successful!")
        logger.info("Logging Successful!")
        return 1
    except:
        print("Logging Failed!")
        logger.info("Logging Failed")
        
    return 0
    


# In[ ]:

if __name__ == '__main__':
    IDs = {'username':USERNAME, 'pwd':PASSWORD, 'loginLink_div':''}
    browsers = {"Chrome":"/usr/bin/chromedriver", "Firefox":"/usr/bin/geckodriver"}
    browser = "Chrome"
    
    # 尝试登录次数
    T = 5
    res = 0
    total_try_cnt = 0
    
    # 一直在后台监视
    while True:
        # 如果当前未连网
        print("=======================================================")
        logger.debug("=======================================================\n")
        try_cnt = 0
        while not is_connected(REMOTE_SERVER):
            try_cnt += 1
            total_try_cnt += 1
            print("Trying to log in the UCAS for {}st".format(try_cnt))
            logger.info("Trying to log in the UCAS for {}st".format(try_cnt))
            
            if browser == 'Chrome':
                driver = webdriver.Chrome(executable_path=browsers[browser])
            else:
                driver = webdriver.Firefox(executable_path=browsers[browser])
                
            res = login_main(driver, URL, IDs)
            driver.close()
            if res < 0 or try_cnt > T:
                break
        # 输入有误        
        if res < 0:
            break;
        
        # 尝试登录次数过多,5分钟后继续尝试登录
        # 登录成功，每隔１分钟检测连网状态
        if try_cnt > T:
            print("Sorry, trying too many times, please try again later!")
            print("Maybe you are in arrears!")
            logger.info("Sorry, trying too many times, please try again later!")
            time.sleep(300)
        elif try_cnt > 0:
            print("Enjoy your time!")
            logger.info("Enjoy your time!")
            time.sleep(60)
        else:
            time.sleep(60)
    print("the service is closed!")
    logger.info("the service is closed!")


# In[ ]:



