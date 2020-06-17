# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:07:52 2019

@author: Marco
"""

from selenium import webdriver
import re
import pandas as pd
import os
import urllib.request
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


''' *****************  ''
    Hong Kong discuss
''  ***************** '''

def get_content_link(link):
    browser.get(link)
    post = browser.find_elements_by_class_name('t_msgfont')
    post = [p.text for p in post]
    post = [[x for x in p.split('\n') if len(x)>0][2:] if '發表' in p else [p] for p in post]
    post = list(set([x for lx in post for x in lx]))
    url = browser.find_elements_by_class_name('next')
    return post,url

chrome_driver_path = 'D:\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(chrome_driver_path)
webpage = ['https://www.discuss.com.hk/index.php']
keyword = '虛擬銀行'
comments = []

browser.get(webpage[0])
browser.find_element_by_id('header-search-text').send_keys(keyword)
browser.find_element_by_class_name('search-button').click()
url = [browser.current_url]

while len(url)>0:
    url = browser.find_elements_by_class_name('next') # search result page
    title = browser.find_elements_by_class_name('search-result-subject')
    message = browser.find_elements_by_class_name('search-result-message')
    
    links = []
    # get information and detail link in the same result page
    for i in range(len(title)):
        if keyword in title[i].text:
            comments.append(title[i].text)
            links.append(browser.find_element_by_link_text(title[i].text).get_attribute('href'))
        else:
            comments.append(message[i].text)
    
    # in each detail link
    for link in links:
        browser.get(link)
        time.sleep(10)
        post, url0 = get_content_link(link)
        while len(url0)>0:
            url0 = list(set([u.get_attribute('href') for u in url0]))
            post2, url0 = get_content_link(url0[0])
        comments.extend(post+post2)
    
    # if next page exist, go to next page
    if len(url)>0:
        url = list(set([u.get_attribute('href') for u in url]))
        browser.get(url[0])



# %%
''' *****************  ''
    Google Play
''  ***************** '''
chrome_driver_path = 'D:\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(chrome_driver_path)
'''
link = {'AlipayHK':    'https://play.google.com/store/apps/details?id=hk.alipay.wallet&hl=en&showAllReviews=true',
     'inMotion':  'https://play.google.com/store/apps/details?id=com.citic.inmotion&hl=en&showAllReviews=true',
     'PayMe':     'https://play.google.com/store/apps/details?id=hk.com.hsbc.paymefromhsbc&hl=en&showAllReviews=true',
     'BEA'  :     'https://play.google.com/store/apps/details?id=com.mtel.androidbea&hl=en&showAllReviews=true',
     'BOC'  :     'https://play.google.com/store/apps/details?id=com.bochk.com&hl=en&showAllReviews=true',
     'BoC Pay':   'https://play.google.com/store/apps/details?id=com.bochk.bocpay&hl=en&showAllReviews=true',
     'Citibank HK': 'https://play.google.com/store/apps/details?id=com.citibank.mobile.hk&hl=en&showAllReviews=true',
     'Dah Sing Bank': 'https://play.google.com/store/apps/details?id=com.MobileTreeApp&hl=en&showAllReviews=true',
     'DBS Omni':  'https://play.google.com/store/apps/details?id=com.compass.rewards&hl=en&showAllReviews=true',
     'DBS Digital Bank': 'https://play.google.com/store/apps/details?id=com.dbs.hk.dbsmbanking&hl=en&showAllReviews=true',
     'ICBC' : 'https://play.google.com/store/apps/details?id=com.icbc.mobile.abroadbank&hl=en&showAllReviews=true',
     'SC': 'https://play.google.com/store/apps/details?id=com.scb.breezebanking.hk&hl=en&showAllReviews=true',
     'Heng Seng': 'https://play.google.com/store/apps/details?id=com.hangseng.rbmobile&hl=en&showAllReviews=true',
     'HSBC': 'https://play.google.com/store/apps/details?id=hk.com.hsbc.hsbchkmobilebanking&hl=en&showAllReviews=true',
     'CCB': 'https://play.google.com/store/apps/details?id=com.ccb.InternationalMobileBanking&hl=en&showAllReviews=true',
     'CMB': 'https://play.google.com/store/apps/details?id=com.wlb.android&hl=en&showAllReviews=true',
     'BankMobile':'https://play.google.com/store/apps/details?id=com.higherone.mobile.android&hl=en&showAllReviews=true',
     'N26':'https://play.google.com/store/apps/details?id=de.number26.android&hl=en&showAllReviews=true',
     'Revolut': 'https://play.google.com/store/apps/details?id=com.revolut.revolut&hl=en&showAllReviews=true',
     'Monzo': 'https://play.google.com/store/apps/details?id=co.uk.getmondo&hl=en&showAllReviews=true'}
'''

browser.get('https://play.google.com/store/apps/details?id=com.citic.inmotion&hl=en&showAllReviews=true')

js = 'return action=document.body.scrollHeight'
n = 0
for i in range(0,5000):
    try:
        webElem = browser.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div')
        webElem.click()
    except:
        # scroll down the page iteratively with a delay
        browser.execute_script("window.scrollTo(0,2500000)")
        time.sleep(3)
        
    if (i+1) % 10 == 0:
        try:
            # Decide whether the height of brower changes
            height = browser.execute_script(js)
            print(height, '  pre->  ', height_pre)
            if height == height_pre and n < 2:
                n += 1
                height_pre = height
                browser.execute_script("window.scrollTo(0,"+str(height-1250)+')') #'1250'
                time.sleep(5)
            elif n == 2 or height>1000000:
                break
            else:
                n = 0
                height_pre = height
        except:
            print('error: ',i)
            break

# Post date and rank are JS element and therefore can't be scratched directly, need to extract from html source code
html = browser.page_source
return_list = html.split('<div aria-label="Rated ')[2:]
rank = []
post_date = []
for i in range(len(return_list)):
    try:
        post_date.append(return_list[i].split('<span class="p2TkOb">')[1].split('</span>')[0])
        rank.append(int(return_list[i][0]))
    except:
        break

# Comment can be collected directly
webElem  = browser.find_elements_by_class_name("UD7Dzf")
web_text = [x.text for x in webElem]
text2 = html.split('<span jsname="fbQN7e" style="display: none;">')[1:]
text2 = [t.split('</span>')[0] for t in text2]
for i in range(len(text2)):
    if text2[i] == '':
        text2[i] = web_text[i]
        
df = pd.DataFrame({'Date':post_date, 'comment':text2, 'rank':rank})
df['bank'] = 'inMotion'
