import os.path
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
localPagePath = ROOT_DIR + "/" + "simple-page/index.html"

driver.get(url="file://" + localPagePath)

def check1(driver1):
    return driver1.find_element(By.CLASS_NAME, "extra1")

print("Czekam 15 max 15 sekund na pojawienie się element z klasą 'exatra1'")
WebDriverWait(driver, timeout=15).until(check1)

print("Operacja powiodła się")

time.sleep(1)
