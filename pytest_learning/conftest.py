import pytest
from selenium import webdriver
import time
driver=webdriver.Chrome()
@pytest.fixture(scope='module')
def Start():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://171.34.197.243:8082/ZHHB/page/login.html')
    driver.find_element_by_id('admin').send_keys('superstart')
    driver.find_element_by_id('password').send_keys('yshb@123..')
    logins = driver.find_element_by_xpath('/html/body/div/div[5]/div[4]/div')
    logins.click()
    time.sleep(2)