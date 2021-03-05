
import pytest
from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import os
driver=webdriver.Chrome()
driver.get('http://171.34.197.243:8082/ZHHB/page/menu.html')
driver.maximize_window()
sleep(2)
driver.find_element_by_id('admin').send_keys('superstart')
driver.find_element_by_id('password').send_keys('yshb@123..')
login=driver.find_element_by_xpath('/html/body/div/div[5]/div[4]/div')
login.click()
sleep(5)
'''driver.find_element_by_class_name('swiper-slide swiper-slide-thumb-active swiper-slide-visible swiper-slide-active').click()#点击污染源在线监测系统
sleep(3)
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/ul/li[2]/ul/li[3]').click()#点击数据查询
sleep(5)'''
driver.get('http://171.34.197.243:8082/wryzxjc/dist/index.html#/')
sleep(3)
driver.get('http://171.34.197.243:8082/wryzxjc/dist/index.html#/DateQuery')
driver.refresh()
sleep(2)
wryqy1=driver.find_element_by_class_name('history_xl_ul')
ActionChains(driver).move_to_element(wryqy1).perform()
qiye1=driver.find_elements_by_xpath('/html/body/div/div[2]/div/div[2]/div[3]/div[2]/div/div[2]')
qiye1.click()
sleep(1)
driver.find_element_by_class_name('export_btn').click()
sleep(5)

