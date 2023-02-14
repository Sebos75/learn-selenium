import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get(url='https://inpost.pl/znajdz-paczkomat')

# Szklarska Poręba
Map_coordinates = dict({
    "latitude": 50.83006771178479,
    "longitude": 15.529813553716314,
    "accuracy": 100
})



driver.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)


time.sleep(.2)
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
time.sleep(.2)

driver.find_element(By.CLASS_NAME, 'getMyCurrentPositionTrigger').click()

time.sleep(10)