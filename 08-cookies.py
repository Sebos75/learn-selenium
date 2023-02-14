import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(url='https://x-kom.pl')

# driver.delete_all_cookies()

driver.add_cookie({"name": "secondName", "value": "Tarkowski"})

cookies = driver.get_cookies()
print(cookies)

# one cookie
cookie = driver.get_cookie("secondName")
print(cookie)
time.sleep(2)
