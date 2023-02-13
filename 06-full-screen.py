import os
import time
from selenium import webdriver

driver = webdriver.Chrome()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
localPagePath = ROOT_DIR + "/" + "simple-page/index.html"

driver.get(url="file://" + localPagePath)
driver.fullscreen_window()
time.sleep(2)
