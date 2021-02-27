from selenium import webdriver
import time
from time import  sleep
import unittest
username='superstart'
passwd='yshb@123..'
url='http://171.34.197.243:8081/ZHHB/page/login.html'
driver=webdriver.chrome



class Test_yshb(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.chrome


