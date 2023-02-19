import timeit
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mysql.connector

class Service:
    def saveFile(self, text):
        outpupFile = '/mnt/gitlab/sof-test/pub/unisoft-wan.log'
        # outpupFile = 'unisoft.log'
        f = open(outpupFile, 'a')
        f.write(text)
        f.close()

    def sendLog(self, name, score):
        self.mydb = mysql.connector.connect(
            host="192.168.2.112",
            database="logs",
            user="logs",
            password="log$",
            autocommit=True
        )
        self.mycursor = self.mydb.cursor()
        sql = "INSERT INTO webapp (event_time, app_name, score) VALUES (now(), %s, %s)"
        val = (name, score)
        self.mycursor.execute(sql, val)

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
        name2 = name.ljust(25,' ')
        message = name2 + "; " + czas + '; ' + str(diff) + '\n'
        self.saveFile(message)
        self.sendLog(name=name, score=diff)
        self.driver.quit()
        return diff



service = Service()
service.saveFile('---------------------------------------------------------------------------\n')
service.get(name='unisoft.com.pl',url='https://www.unisoft.com.pl')
service.get(name='sof.unisoft.com.pl',url='https://sof.unisoft.com.pl')
service.get(name='bug.unisoft.com.pl',url='https://bug.unisoft.com.pl')
service.get(name='portal.unisoft.com.pl',url='https://portal.unisoft.com.pl/login')
service.get(name='epracownik.unisoft.com.pl',url='https://epracownik.unisoft.com.pl')
service.get(name='crm.unisoft.com.pl',url='https://crm.unisoft.com.pl/crm2/Default.aspx')
