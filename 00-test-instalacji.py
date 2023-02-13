import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url='https://google.com')
time.sleep(3)
