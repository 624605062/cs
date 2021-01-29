from selenium import webdriver
import time
driver = webdriver.Chrome() #打开浏览器
driver.get("http://171.34.197.243:8081/yshbOperation/dist/index.html#/systemManagement/userManagement") #访问url
driver.maximize_window() #最大化窗口