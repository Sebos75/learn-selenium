import os
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
localPagePath = ROOT_DIR + "/" + "simple-page/index.html"

driver.get(url="file://" + localPagePath)

imieElement = driver.find_element(By.ID,'first-name')
time.sleep(1)
imieElement.send_keys('Jan')

nazwiskoElement = driver.find_element(By.ID,'second-name')
time.sleep(1)
nazwiskoElement.send_keys('Nowak')
time.sleep(1)
nazwiskoElement.send_keys(Keys.ENTER)
time.sleep(3)
