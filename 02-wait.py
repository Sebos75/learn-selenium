import os.path
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2) # ustawia globalny timeout (dla wyszstkich żądań)
#https://testelka.pl/implicit-oraz-explicit-wait/


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
localPagePath = ROOT_DIR + "/" + "simple-page/index.html"

driver.get(url="file://" + localPagePath)

print("Czekam max 2 sekundy na pojawienie się element z klasą 'exatra1'")
element = driver.find_element(By.CLASS_NAME, "extra1")

print("Operacja powiodła się")

time.sleep(1)
