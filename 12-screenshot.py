import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url='https://www.x-kom.pl/goracy_strzal')

driver.find_element(By.CLASS_NAME, 'dRLEBj').click()
time.sleep(1)

price = driver.find_element(By.CLASS_NAME, 'iTupOL')
print(price.text)

driver.save_screenshot('full.png')

detailElement = driver.find_element(By.CLASS_NAME, 'ffWNLr')
detailElement.screenshot('detail.png')

time.sleep(2)
