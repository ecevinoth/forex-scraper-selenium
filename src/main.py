from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def scrap(**kwargs):
    try:
        options = Options()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
        driver.get(kwargs['url'])
        value = driver.find_element_by_xpath(kwargs['xpath']).text
        duration = datetime.now() - start_date
        driver.quit()

        if kwargs['label'] == 'uae_xchange':
            value = value.split()[3]
        elif kwargs['label'] == 'instarem':
            value = float((value.split()[0]).replace(',', ''))/1000
        else:
            value = value
        return f"{value},{kwargs['label']},{duration}"

    except Exception as e:
        print("Exception found: \n", format(e))


if __name__ == "__main__":
    start_date = datetime.now()

    rate_xe = scrap(label="xe", url="http://www.xe.com/currencyconverter/convert/?Amount=1&From=MYR&To=INR", xpath='//*[@id="converterResult"]/div/div/div[2]/span[1]')
    rate_moneymatch = scrap(label="MoneyMatch", url="https://transfer.moneymatch.co/utility/rate/MYR/INR", xpath='/html/body')
    rate_uae = scrap(label="uae_xchange", url="https://my.uaeexchange.com/", xpath='//*[@id="exchange-rate-calc"]')
    rate_instarem = scrap(label="instarem", url="https://www.instarem.com/currency-converter/myr-to-inr", xpath='//*[@id="currency_you_receive"]')
    rate_transferwise = scrap(label="transferwise", url="https://transferwise.com/gb/currency-converter/myr-to-inr-rate", xpath='/html/body/main/section/div[2]/div[1]/div/form/div[2]/div[1]/h3/span[3]')

    print(f"{rate_xe}\n{rate_moneymatch}\n{rate_uae}\n{rate_instarem}\n{rate_transferwise}")
    # eremit = scrap1("https://api.eremit.com.my/EremitService.svc/GetExchangeRates")
