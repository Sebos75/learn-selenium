import timeit
from selenium import webdriver
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.chrome.options import Options


start = timeit.default_timer()

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(options=options)
print_options = PrintOptions()
print_options.page_ranges = ['1-2']

driver.get(url='https://gmail.com')

driver.print_page()
base64code = driver.print_page(print_options)
print(base64code)

stop = timeit.default_timer()

print("czas wykonania: ", stop - start)