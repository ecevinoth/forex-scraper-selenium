import os
import sys
import threading
from datetime import datetime

from selenium import webdriver


def scrap(agency):
    start_time = datetime.now()
    os.environ['MOZ_HEADLESS'] = '1'
    driver = webdriver.Firefox()
    driver.get(agency['url'])
    try:
        scrap_string = driver.find_element_by_xpath(agency['xpath']).text
    except Exception as e:
        print("Exception found: \n", format(e))
        print(f"*not* found the xpath element.")
    finally:
        print(f"found the xpath element, run duration {(datetime.now() - start_time).seconds} seconds.")
        driver.close()
        driver.quit()

    if agency['label'] == 'uae_xchange':
        rate = scrap_string.split()[3]
    elif agency['label'] == 'instarem':
        rate = float((scrap_string.split()[0]).replace(',', '')) / 1000
    elif agency['label'] == 'lotus_remit':
        rate = scrap_string.split()[2]
    else:
        rate = scrap_string

    print(f"{float(rate).__round__(4):2.04f}, {agency['label']}")
    return f"{float(rate).__round__(4):2.04f}, {agency['label']}"


if __name__ == "__main__":
    start_time_main = datetime.now()
    dictionary = {
        'xe': {'label': "xe",
               'url': "http://www.xe.com/currencyconverter/convert/?Amount=1&From=MYR&To=INR",
               'xpath': '//*[@id="converterResult"]/div/div/div[2]/span[1]'},
        "MoneyMatch": {"label": "MoneyMatch",
                       "url": "https://transfer.moneymatch.co/utility/rate/MYR/INR",
                       "xpath": '/html/body'},
        "uae_xchange": {"label": "uae_xchange", "url": "https://my.uaeexchange.com/",
                        "xpath": '//*[@id="exchange-rate-calc"]'},
        "instarem": {"label": "instarem",
                     "url": "https://www.instarem.com/currency-converter/myr-to-inr",
                     "xpath": '//*[@id="currency_you_receive"]'},
        "transferwise": {"label": "transferwise",
                         "url": "https://transferwise.com/gb/currency-converter/myr-to-inr-rate",
                         "xpath": '/html/body/main/section/div[2]/div[1]/div/form/div[2]/div[1]/h3/span[3]'},
        "lotus_remit": {"label": "lotus_remit", "url": "https://www.lotusremit.com/Rates.aspx",
                        "xpath": '//*[@id="gvRates"]/tbody/tr[3]'},
    }
    threads = [threading.Thread(target=scrap, args=(dictionary[agency],)) for agency in dictionary]
    threads_start = [thread.start() for thread in threads]
    threads_join = [thread.join() for thread in threads]

    # eremit = scrap1("https://api.eremit.com.my/EremitService.svc/GetExchangeRates")
    print(f'"{sys.argv[0].split("/")[-1]}" script completed successfully. Total run time : {(datetime.now() - start_time_main).seconds}')
