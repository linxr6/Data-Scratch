# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:18:23 2020

@author: Marco
"""

import fxcmpy 
import pandas as pd
from datetime import datetime, timedelta
import os

os.chdir('D:\\FX')
TOKEN = '858f38c91f7e718f796d6e0e782653f42eb149d5'
con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error', server='demo', log_file='log.txt')
instruments = con.get_instruments()

# period must be one of ['m1', 'm5', 'm15', 'm30', 'H1', 'H2', 'H3', 'H4', 'H6', 'H8', 'D1', 'W1', 'M1']
periods = ['H4','D1','M1']   #'m5',,'H2','H4','D1']

item = ['EUR/USD', 'GBP/USD', 'USD/JPY', 'USD/CAD', 'AUD/USD', 'NZD/USD', 'USD/CHF',
        'EUR/GBP', 'EUR/JPY', 'GBP/JPY', 'EUR/AUD', 'GBP/AUD', 'AUD/NZD', 
        'JPN225', 'FRA40', 'GER30', 'NAS100', 'SPX500', 'UK100',
        'USDOLLAR', 'USOil', 'NGAS', 'XAU/USD']


start = datetime(2015, 1, 1)
end = datetime(2020, 4, 28)
        
for period in periods:
    for key in item:
        data = con.get_candles(key, period=period, start=start, end=end)
        key = key.replace('/','-')
        data.to_excel('D:\\FX\\'+period+'\\'+'H4_'+key+'.xlsx')
        

# %%  Data Preprocessing

for key in item:
    key = key.replace('/','-')
    data = pd.read_excel('D:\\FX\\'+'monthly'+'\\'+'M_'+key+'.xlsx')
    data['month'] = data['date'].dt.month
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        