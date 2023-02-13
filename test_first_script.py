import time
from selenium import webdriver


def test_eight_components():
    driver = webdriver.Chrome()
    driver.get(url='https://www.x-kom.pl/')
    title = driver.title
    print(title)

    time.sleep(5)

    driver.quit()


test_eight_components()