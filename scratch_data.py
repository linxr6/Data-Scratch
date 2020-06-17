# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:07:52 2019

@author: Cynthia
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
import matplotlib.pyplot as plt
import cv2
import numpy as np
from django.utils import encoding

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



''' *****************  ''
         LIHKG
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
webpage = ['https://lihkg.com/search?q=虛擬銀行']
keyword = '虛擬銀行'
comments = []

browser.get(webpage[0])
drag = browser.find_element_by_xpath('//*[@id="leftPanel"]')
from selenium.webdriver.common.action_chains import ActionChains
for _ in range(0, 50):
    ActionChains(browser).drag_and_drop_by_offset(drag,0,100).perform()
        #browser.execute_script("window.scrollTo(0, 150000);")
    time.sleep(5)








//*[@id="leftPanel"]/div[2]/div[1]/div[1]/div[2]/div/div/span
//*[@id="leftPanel"]/div[2]/div[2]/div[1]/div[2]/div/div/span
//*[@id="leftPanel"]/div[2]/div[3]/div[1]/div[2]/div/div/span

<a class="_2A_7bGY9QAXcGu1neEYDJB" href="/thread/787121/page/1"></a>
<span class="_20jopXBFHNQ9FUbcGHLcHH">[入侵]小米香港開銀行，正在申請虛擬銀行牌照</span>




''' *****************  ''
    Google Play
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
webpage = 'https://play.google.com/store/apps/details?id='
id_w = 'com.citic.inmotion'
webpage = webpage+id_w
comments = []

browser.get(webpage)
browser.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[6]/div').click()
stars = browser.find_element_by_class_name("pf5lIe")

stars = [s.text for s in stars]

comments = browser.find_elements_by_class_name("UD7Dzf")
comments = [w.text for w in comments]

browser.find_element_by_id('gbqfq').send_keys(keyword)
browser.find_element_by_id('gbqfb').click()
url = [browser.current_url]

browser.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[6]/div/span/span')
//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[6]/div/span/span
//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/div[1]/div/div/div[1]/div[6]/div/span/span
//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/span/span
//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/span/span      

link=links[0]
    
    

browser.back()
browser.forward()
browser.refresh()


# find and click
webElem = browser.find_element_by_xpath()
webElem.click()
webElem.text

# %%
''' *****************  ''
    Google Play
''  ***************** '''
#from selenium.webdriver.chrome.options import Options
chrome_driver_path = 'D:\\chromedriver_win32\\chromedriver.exe'
#chrome_options = Options()
#chrome_options.add_argument('--dns-prefetch-diable')
browser = webdriver.Chrome(chrome_driver_path)

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


browser.get('https://play.google.com/store/apps/details?id=com.citic.inmotion&hl=en&showAllReviews=true')

# scroll down the page iteratively with a delay
# Decide whether the height of brower changes
js = 'return action=document.body.scrollHeight'
height_pre = browser.execute_script(js)
n = 0
for i in range(0,5000):
    try:
        webElem = browser.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div')
        webElem.click()
    except:
        browser.execute_script("window.scrollTo(0,2500000)")
        time.sleep(3)
        
    if (i+1) % 10 == 0:
        try:
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
            

# 
'''
post_date = []
rank = []
text2 = []
error_list = []
webElem  = browser.find_elements_by_class_name("UD7Dzf")
full_review = browser.find_elements_by_xpath('//button[contains(text(), "Full Review")]')
for i in range(len(full_review)):
    try:
        full_review[i].click()
        time.sleep(5)
    except:
        print('error: ',i)
    
for i in range(1,len(webElem)+1):
    try:
        cl = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[1]/div[1]/div'
        webElem_ = browser.find_element_by_xpath(cl)
        post_date.append(webElem_.text)
        
        xp = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[1]/div[1]/div/span[1]/div/div'
        webElem_ = browser.find_element_by_xpath(xp).get_attribute('aria-label')
        rank.append(int(webElem_.split(' ')[1]))
        
        tp = '//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div['+str(i)+']/div/div[2]/div[2]/span[2]'
        webElem_ = browser.find_element_by_xpath(tp)
        if webElem_.text == '':
            tp = tp.replace('span[2]', 'span[1]')
            webElem_ = browser.find_element_by_xpath(tp)
        text2.append(webElem_.text)
        print('successful: ', i)
    except:
        error_list.append(i)
        print('error: ', i)
'''

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

webElem  = browser.find_elements_by_class_name("UD7Dzf")
web_text = [x.text for x in webElem]
text2 = html.split('<span jsname="fbQN7e" style="display: none;">')[1:]
text2 = [t.split('</span>')[0] for t in text2]
for i in range(len(text2)):
    if text2[i] == '':
        text2[i] = web_text[i]
        
dfx = pd.DataFrame({'Date':post_date, 'comment':text2, 'rank':rank})
dfx['bank'] = 'inMotion'

df = pd.concat([df,dfx])

d = {'AlipayHK':    'https://play.google.com/store/apps/details?id=hk.alipay.wallet&hl=en&showAllReviews=true',
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

df_en = df_en.reset_index(drop=True)

target = []
for i in range(len(df_en)):
    if df_en['bank'][i]=='Revolut' or df_en['bank'][i]=='Monzo Bank' or df_en['bank'][i]=='N26':
        target.append('VB')
    else:
        target.append('HK Bank')
df_en['target'] = target

#flag = []
#for i in range(0,10):
#    try:
#        webElem = browser.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[2]/div')
#        webElem.click()
#        time.sleep(2)
#        browser.execute_script("window.scrollTo(0,150000)")
#        time.sleep(2)
#    except:
#        browser.execute_script("window.scrollTo(0,150000)")
#        time.sleep(2)
#    if (i+1) % 10 == 0:
#        web_text  = browser.find_elements_by_class_name("UD7Dzf")
#        web_text = [x.text for x in web_text]
#        if len(flag) == 0:
#            flag.append(len(web_text))
#        else:
#            if len(web_text) == flag[-1]:
#                break
#            else:
#                flag.append(len(web_text))
#    print(i)

# %%
from selenium import webdriver
import pandas as pd
import os
import time
from selenium.webdriver.common.by import By
from collections import defaultdict

chrome_driver_path = 'D:\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(chrome_driver_path)
data = defaultdict(list)

for i in range(1,55):
    link = 'http://www.soupu.com/pinpai/list.aspx?byt=6&syt=606&pptype=0&page='+str(i)
    browser.get(link)
    time.sleep(5)
    for j in range(10):
        tableId = "ctl00_main_repALL_ctl0"+str(j)+"_divContent"
        try:
            table_loc = (By.ID,tableId)
            table_list = browser.find_element(*table_loc).find_elements(By.TAG_NAME, "tr")
            data['品牌'].append(table_list[0].text)
            data['公司名称'].append(table_list[1].text.split()[0].split('：')[-1])
            data['公司地址'].append(table_list[1].text.split()[-1].split('：')[-1])
            data['业态'].append(table_list[2].text.split()[0].split('：')[-1])
            data['需求面积'].append(table_list[2].text.split()[-1].split('：')[-1])
            data['拓展区域'].append(table_list[3].text.split()[0].split('：')[-1])
            data['合作期限'].append(table_list[3].text.split()[-1].split('：')[-1])
        except:
            pass
    print('Complete page: ', i)
    
df = pd.DataFrame(data)
df.to_excel('C:\\Users\\Cynthia\\Desktop\\搜铺品牌信息.xlsx')
  

import bs4
import requests
from collections import defaultdict
import pandas as pd
import time

data = defaultdict(list)
for j in range(1,55):
    link = 'http://www.soupu.com/pinpai/list.aspx?byt=6&syt=606&pptype=0&page='+str(j)
    html_page = requests.get(link)
    hp = html_page.text
    soup = bs4.BeautifulSoup(hp)
    table_list = soup.find_all('table')
    for i in range(len(table_list)):
        data['品牌'].append(table_list[i].find_all('tr')[0].find_all('td')[-1].text.strip())
        data['公司名称'].append(table_list[i].find_all('tr')[1].find_all('td')[0].text.split('：')[-1].strip())
        data['公司地址'].append(table_list[i].find_all('tr')[1].find_all('td')[-1].text.split('：')[-1].strip())
        data['业态'].append(table_list[i].find_all('tr')[2].find_all('td')[0].text.split('：')[-1].strip())
        data['需求面积'].append(table_list[i].find_all('tr')[2].find_all('td')[-1].text.split('：')[-1].strip())
        data['拓展区域'].append(table_list[i].find_all('tr')[3].find_all('td')[0].text.split('：')[-1].strip())
        data['合作期限'].append(table_list[i].find_all('tr')[3].find_all('td')[-1].text.split('：')[-1].strip())
    print('Complete page: ', j)
    time.sleep(5)

df = pd.DataFrame(data)
df.to_excel('搜铺品牌信息')