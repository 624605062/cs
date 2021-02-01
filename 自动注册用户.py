from selenium import webdriver
import time
from time import  sleep
import unittest
from selenium.webdriver.common.action_chains import ActionChains
#登录系统
driver = webdriver.Chrome() #打开浏览器
driver.get("http://171.34.197.243:8081/ZHHB/page/login.html") #访问url
 #最大化窗口
driver.maximize_window()
sleep(3)
###登录用户
driver.find_element_by_xpath('/html/body/div/div[5]/div[1]/div/input').send_keys('super')
driver.find_element_by_id('password').send_keys('11111111')
driver.find_element_by_class_name('logbtn').click()
##等待10秒 手动输入验证
######进入污染源系统
sleep(3)
driver.get('http://171.34.197.243:8081/wryzxjc/dist/index.html#/')

