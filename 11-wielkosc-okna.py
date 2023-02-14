import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(url="https://gmail.com")

size = driver.get_window_size()
print(size)

width = size.get("width")
height = size.get("height")

print(width, height)
time.sleep(1)

driver.set_window_size(1024,768)
time.sleep(1)
driver.maximize_window()

time.sleep(2)
