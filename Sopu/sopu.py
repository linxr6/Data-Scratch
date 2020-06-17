# -*- coding: utf-8 -*-
"""
Created on Sat May  2 23:32:35 2020

@author: Marco
"""

from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from collections import defaultdict

chrome_driver_path = 'D:\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(chrome_driver_path)
data = defaultdict(list)

for i in range(1,55):
    link = 'http://www.soupu.com/pinpai/list.aspx?byt=6&syt=606&pptype=0&page='+str(i)
    browser.get(link)
    time.sleep(3)
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
df.to_excel('搜铺品牌信息.xlsx')
  
