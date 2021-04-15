import time
import os
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
@pytest.fixture(scope='module',autouse=True)
def Start():
    global driver
    driver = webdriver.Chrome()
    driver.get('http://171.34.197.243:8081/ZHHB/page/login.html')
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_id('admin').send_keys('superstart')
    driver.find_element_by_id('password').send_keys('yshb@123..')
    logins = driver.find_element_by_xpath('/html/body/div/div[5]/div[4]/div')
    logins.click()
    time.sleep(5)
    driver.get('http://171.34.197.243:8081/wryzxjc/dist/index.html#/')
    time.sleep(3)
def test_sjcx():
    driver.get('http://171.34.197.243:8081/wryzxjc/dist/index.html#/DateQuery')
    time.sleep(2)
    driver.find_element_by_class_name('export_btn').click()
    time.sleep(3)
def test_zhtj():
    driver.get('http://171.34.197.243:8081/wryzxjc/dist/index.html#/ComSta')
    time.sleep(2)
    driver.find_element_by_class_name('export_btn').click()
    time.sleep(3)
def test_bbtj():
    driver.get('http://171.34.197.243:8081/wryzxjc/dist/index.html#/IntSta')
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[5]/div[12]').click()
    time.sleep(3)
if __name__ == '__main__':
    pytest.main(['-s','test_dc.py'])

