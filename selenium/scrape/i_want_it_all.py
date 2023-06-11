from selenium import webdriver
from selenium.webdriver.common.by import By
import json

from random import choice
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--log-level=3")
import re

def extract_clean_string(input_string):
    clean_string = re.search(r'^(.+?)\n\d+% off', input_string, re.MULTILINE)
    if clean_string:
        return clean_string.group(1)
    else:
        clean_string= input_string.split('\n')[0]
        if len(clean_string)<len('FEATUREDNOW'):
            clean_string=clean_string+" "+input_string.split('\n')[1]
        return clean_string

    

def process_prices(prices):
    #return discount and sale price and mrp number
    try:
        sale_price = float(prices[0].replace('$', '')) / 100
        mrp = float(prices[1].replace('$', ''))
        discount_percentage = ((mrp - sale_price) / mrp) * 100
        return [sale_price, mrp, "{:.2f}%".format(discount_percentage)]
    except:pass


def web_fetch_data(text):
    try:
        text=text.split('\n')
        meta_price=process_prices([text[-2],text[-1]])
        return meta_price
    except:
        pass


def scrape(driver):
    driver.get('https://www.amazon.com/gp/goldbox/')
    Dox=driver.find_elements(By.CLASS_NAME,'scroll-carousel_slide__1ku-E.scroll-carousel_scrollItemOuter__2LsK9')
    g_metadata=[]
    for elements_here in Dox:
        try:
            meta=web_fetch_data(elements_here.text)
            assert isinstance(meta,list) , 'data is not list'
            meta.insert(0,extract_clean_string(elements_here.text))
            g_metadata.append(meta)
        except:
            pass
    return g_metadata

def save_cookies(driver):#save cookies
    cookies = driver.get_cookies()
    with open('cookies.txt','w') as out_file:
        json.dump(cookies,out_file,indent=4)

#driver code
def driver():
    try:
        driver=webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        return scrape(driver)
    except Exception as e:
        print(e)




# try:
#     with open('cookies.txt','r') as s:
#         cookies=json.load(s)
#     driver.get('https://linkedin.com/')
#     for cookie in cookies:
#         driver.add_cookie(cookie)
#     driver.refresh()
# except Exception as e:
#     print(e)
#     print('generating cookie file after logging in/n')
#     login(driver)


# from itertools import cycle
# def message_file(driver,jj):
#     with open('messages1.txt','r') as s:
#         f=s.readlines()
#         kl=[]#messages
#         for i in f:
#             kl.append(i[:-1])
#         zip_list = zip(jj, cycle(kl)) if len(jj) > len(kl) else zip(cycle(jj), kl)
