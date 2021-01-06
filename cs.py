from selenium import webdriver
import  time
driver = webdriver.Chrome()

driver.get("http://171.34.197.243:8082/yshbOperation/dist/index.html?userName=Sh5PEJPecZEq+dtTg87X3BAWGd73XLR1wf/X1kM4iw6MvYToeNtjWI0CDyNJ24Q/mDGYsms5j5ZSRfeO2gpdzwx0zPoezNSFg4DSLg9846zU7R5fIMT2mKkAZHcTtIlvRZBo/zTY/LCtHzJeQhNMk6AHNN1RFi6byLC7n9903yY=&userPwd=G9xmtG6kq+6awsxdufgcZX7OEvQdNnqG8Zv6BrAzwlhVsLENGyuuyifCvdyjp3aDSjxA1dXIsl3mKO2f0D4E9VzssqLviFcqd4b/ZpP1+d49KZdQl6/A3T4CgIokUOzrF/VnVJIfCleWN5YqpqNUPMWCcQ9Jse7qP3WgoK8ePio=#/systemManagement/userManagement")
time.sleep(5)
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div/div/div/div[1]/div/div[1]/label/div/input").send_keys("江西")
time.sleep(2)
ss=driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div/div/div/div[1]/div/div[1]/button[1]")
ss.click()
time.sleep(2)
bj=driver.find_element_by_xpath("/html/body/div/div/div[2]/div[3]/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[8]/button[1]")
bj.click()
