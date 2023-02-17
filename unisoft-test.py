import time
import timeit
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Service:
    def get(self,name, url):

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  #

        self.driver = webdriver.Chrome(options=options)
        start = timeit.default_timer()
        self.driver.get(url=url)
        stop = timeit.default_timer()
        diff = stop - start
        print(name,diff)
        now = datetime.now()
        czas = now.isoformat(sep=' ')
        name2 = name.ljust(28,' ')
        message = name2 + "; " + czas + '; ' + str(diff) + '\n'
        self.driver.quit()
        f = open('unisoft.log', 'a')
        f.write(message)
        f.close()
        return diff



service = Service()
# while(True):
service.get(name='unisoft.com.pl',url='https://www.unisoft.com.pl')
service.get(name='sof.unisoft.com.pl',url='https://sof.unisoft.com.pl')
service.get(name='bug.unisoft.com.pl',url='https://bug.unisoft.com.pl')
service.get(name='portal.unisoft.com.pl',url='https://portal.unisoft.com.pl/login')
service.get(name='epracownik.unisoft.com.pl',url='https://epracownik.unisoft.com.pl')
service.get(name='crm.unisoft.com.pl',url='https://crm.unisoft.com.pl/crm2/Default.aspx')
