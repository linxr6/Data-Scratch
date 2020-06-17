# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 01:18:12 2018

@author: Marco
"""

import pandas as pd
from selenium import webdriver
import time
from datetime import datetime
import os
os.chdir('C:\\Users\\Administrator\\Desktop\\sem1\\STAT7008\\project')

def get_tweets(start,end):
    link = 'https://twitter.com/search?vertical=default&q=from%3ArealDonaldTrump%20since%3A'+start+'%20until%3A'+end+'&src=typd'
    driver.get(link)
    # scroll down the page iteratively with a delay
    for _ in range(0, 50):
        try:
            driver.execute_script("window.scrollTo(0, 150000);")
            time.sleep(5)
        except:
            break
    
    webElem = driver.find_elements_by_xpath('//div[@class="js-tweet-text-container"]')
    tweets = []
    tweet_time = []

    for i in range(len(webElem)):
        tweets.append(webElem[i].text)
    
    pagetxt=(driver.page_source)  
    page = pagetxt.replace('\n',' ').split('午')
    AM_PM = [text[-1] for text in page]
    am_pm = []
    for ap in AM_PM:
        if ap == '上':
            am_pm.append(0)
        elif ap == '下':
            am_pm.append(12)
        else:
            break
    
    time_list = [text.split('日')[0].replace('年','-').replace('月','-').replace(' - ', ' ') for text in page][1:]
    for i in range(len(time_list)):
        if am_pm[i] == 12:
            hour = time_list[i].split(':')[0]
            hour_num = int(hour) + am_pm[i]
            if hour_num == 24:
                hour_num = 0
            time_list[i] = str(hour_num) + time_list[i][len(hour):] 
    Format = '%H:%M %Y-%m-%d'        
    time_list = [datetime.strptime(t0, Format) for t0 in time_list]
    tweet_df = pd.DataFrame({'tweet':tweets, 'time':time_list})
    
    return(tweet_df)


driver = webdriver.Chrome('E:\chromedriver_win32\chromedriver.exe')

# collect data in each period
start = ['2018-06-01', '2018-01-01', '2017-06-01', '2017-01-01',
         '2016-06-01', '2016-01-01', '2015-06-01', '2015-01-01']       #'2018-06-01'
end = ['2018-12-18', '2018-06-01', '2018-01-01', '2017-06-01',
       '2017-01-01', '2016-06-01', '2016-01-01', '2015-06-01']          #'2018-12-18'

tweet = pd.DataFrame()
for i in range(len(start)):
    tweet_df = get_tweets(start,end)
    tweet = pd.concat([tweet,tweet_df], axis=0)

tweet = tweet.reset_index(drop=True)



