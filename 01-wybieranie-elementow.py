import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url='https://www.x-kom.pl')
time.sleep(.3)


title = driver.title
assert title == "x-kom.pl - Sklep komputerowy"
# okElement = browser.find_element(By.XPATH, '//*[@id="react-portals"]/div[10]/div/div/div/div[3]/button[2]')
okElement = driver.find_element(By.CLASS_NAME, 'dRLEBj')
okElement.click()

# time.sleep(1)
hotElement = driver.find_element(By.CLASS_NAME, 'xdUIb')
hotElement.click()

time.sleep(3)
