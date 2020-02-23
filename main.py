from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup
import os

SaveDirectory = os.getcwd()
webdriver_path = SaveDirectory + '\chromedriver.exe'


keyword = input("想找的職業：")
driver = webdriver.Chrome(executable_path=webdriver_path) #開啟firefox
driver.get("https://www.104.com.tw/jobs/search/?keyword=" + keyword + "order=1&jobsource=2018indexpoc&ro=0") #前往這個網址


# sleep(2)
# driver.find_element_by_name("username").send_keys("itop")
# driver.find_element_by_name("password").send_keys("litv123")
# driver.find_element_by_name("submit").click()
# sleep(2)
# driver.find_element_by_xpath("/html/body/header/nav/div/ul/li[2]/a").click()
# sleep(2)
# driver.find_element_by_xpath("/html/body/section/div/div[1]/div/div/div[2]/div/a").click()
# sleep(2)