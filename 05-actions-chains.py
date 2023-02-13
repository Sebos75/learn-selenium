import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url='https://www.selenium.dev/selenium/web/mouse_interaction.html')

clickableElement = driver.find_element(By.ID, 'clickable')

webdriver.ActionChains(driver)\
    .move_to_element(clickableElement)\
    .click()\
    .send_keys('aaa')\
    .pause(1)\
    .send_keys(' bbb')\
    .perform()

time.sleep(2)