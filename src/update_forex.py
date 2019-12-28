# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:28:28 2018
@author: svrsunil
"""

# -*- coding: utf-8 -*-
# from dbhelper import DBHelper
# db = DBHelper()
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# import schedule

import win32gui
import win32con

class check:
    def scrap0(self, url, label="xe"):
        print("scrap0:" + label)
        try:
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options)
            # win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_MINIMIZE)
            driver.get(url)
            print("Headless Firefox Initialized")
            text = driver.find_element_by_xpath('//*[@id="converterResult"]/div/div/div[2]/span[1]').text
            print("driver connected")
            print(text)
            driver.quit()
        except Exception as e:
            print("Exception found: ", format(e))

    def scrap1(self, url = "", label = "eremit"):
        print("scrap1:" + label)
        q = Request(url)
        q.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
        page = urlopen(q)
        soup = BeautifulSoup(page, 'html.parser')
        #result = str(soup)
        result = json.loads(str(soup))

        for ctr in result['ExchangeRatesList']:
            if('India' in ctr['CountryName']):
               return ctr['ExchangeRate']
               # break;

    # def scrap2(self, url="", label="matchmoney"):
    #     print('scrap2:' + label)
    #     q = Request(url)
    #     q.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
    #     page = urlopen(q)
    #     return BeautifulSoup(page, 'html.parser')

    def scrap3(self, url="", label="money2anywhere"):
        print('scrap3:' + label)
        q = Request(url)
        q.add_header('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5')
        sp = BeautifulSoup(urlopen(q), 'html.parser')
        print(sp.find('span', id="exchange-rate-calc"))
        browser = webdriver.Firefox()
        browser.get(url)
        html_source = browser.page_source
        browser.quit()
        sp1 = BeautifulSoup(html_source)
        print(sp1.find('span', id="exchange-rate-calc"))


if __name__ == "__main__":
    forex = check()
    start_date = datetime.now()
    xe = forex.scrap0("http://www.xe.com/currencyconverter/convert/?Amount=1&From=MYR&To=INR")
    # text = "\n 1) XE : http://www.xe.com 1 MYR = :" + str(xe)

    # eremit = scrap1("https://api.eremit.com.my/EremitService.svc/GetExchangeRates")
    mmrate = scrap2("https://transfer.moneymatch.co/utility/rate/MYR/INR")
    # text = text + "\n 2) E-Remit : http://www.eremit.com.my/ 1 MYR = :" + str(eremit)
    # text = text + "\n 3) Money Match : https://transfer.moneymatch.co/ 1 MYR = :" + str(mmrate)
    # today = str(datetime.today())
    # text = text + "\n On " + today
    # text = text + "\n All Info are crawled from  net, not for commercial purpose. For Live price visit the site.."
    # print(text)
    # db.add_info("forex", text, today)
    # scrap3("htadd_infotps://my.uaeexchange.com/")
    print(datetime.now() - start_date)
