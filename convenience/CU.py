from selenium import webdriver
from time import sleep
import selenium


url = 'http://cu.bgfretail.com/event/plus.do?category=event&depth1=3&sf=N'
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe', chrome_options=options)
driver.get(url)

try:
    while driver.find_element_by_link_text("더보기"):
        try:
            driver.find_element_by_link_text("더보기").click()
            print("request more page...")
        except selenium.common.exceptions.StaleElementReferenceException:
            sleep(1)
            print("wait 1 second...")
        except selenium.common.exceptions.ElementClickInterceptedException:
            sleep(1)
            print("wait 1 second...")
except selenium.common.exceptions.NoSuchElementException:
    with open('CU_salesList.txt', 'w+', encoding='utf-8') as f:
        for p in driver.find_elements_by_class_name('prodName'):
            if p.find_element_by_xpath("./..").text == '':
                pass
            else:
                prod = p.find_element_by_xpath("./..").text.split('\n')
                f.write(str({'prodName': prod[0],
                             'prodPrice': prod[1],
                             'prodBonus': prod[2]}) + ', ')
