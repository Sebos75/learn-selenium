import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
localPagePath = ROOT_DIR + "/" + "simple-page/index.html"

driver.get(url="file://" + localPagePath)

addElement = driver.find_element(By.ID, 'add-btn')
imieElement = driver.find_element(By.ID, 'first-name')

webdriver.ActionChains(driver) \
    .pause(2) \
    .move_to_element(addElement) \
    .pause(1) \
    .move_to_element(imieElement) \
    .perform()
time.sleep(2)
