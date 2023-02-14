import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
localPagePath = ROOT_DIR + "/" + "simple-page/index.html"

driver.get(url="file://" + localPagePath)
time.sleep(3)
subElement = driver.find_element(By.ID, 'submit-btn').click()

time.sleep(1)
driver.back()
driver.refresh()

#driver.fullscreen_window()
driver.execute_script('window.open()')
time.sleep(1)
handles = driver.window_handles
print(handles)

driver.switch_to.window(handles[1])
driver.get(url='https://gmail.com')

driver.execute_script('alert(\'Koniec!!\')')

# window.scrollTo({
#   top: document.body.scrollHeight,
#   left: 100,
#   behavior: 'smooth'
# });

time.sleep(2)




time.sleep(2)