import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://171.34.197.243:8082/ZHHB/page/login.html')
driver.find_element_by_id('admin').send_keys('superstart')
driver.find_element_by_id('password').send_keys('yshb@123..')
login = driver.find_element_by_xpath('/html/body/div/div[5]/div[4]/div')
login.click()
time.sleep(5)
save_cookie = driver.get_cookies()
print(save_cookie)
driver.quit()
driver1 = webdriver.Chrome()
driver1.maximize_window()
driver1.get('http://171.34.197.243:8082/ZHHB/page/login.html')
print(driver1.get_cookies())
driver1.delete_all_cookies()
for cookie in save_cookie:
    driver1.add_cookie(cookie)
driver1.get('http://171.34.197.243:8082/wryzxjc/dist/index.html#/')
print(driver1.get_cookies())
time.sleep(3)
driver.refresh()
driver.get('http://171.34.197.243:8082/wryzxjc/dist/index.html#/DateQuery')
driver.refresh()
time.sleep(2)
wryqy1 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[3]/div[2]')
ActionChains(driver).move_to_element(wryqy1).perform()
qiye1 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[3]/div[2]/span')
qiye1.click()
time.sleep(2)
driver.find_element_by_class_name('export_btn').click()
time.sleep(2)