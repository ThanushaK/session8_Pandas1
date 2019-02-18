# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 21:33:06 2019

@author: thanusha
"""

import pandas as pd 
import numpy as np       
df =pd.DataFrame({'X' :[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
#1        
izero = np.r_[-1, (df['X'] == 0).nonzero()[0]] # indices of zeros
idx = np.arange(len(df)) #creating an array whose length is equal to length of dataframe
df['Y'] = idx - izero[np.searchsorted(izero - 1, idx) - 1] #elements of idx array are inserted and sorted into izero array
#making it has column Y
print(df['Y'])
#2
dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B') #using daterange between specified period with a frequency of business day 
s = pd.Series(np.random.rand(len(dti)), index=dti) #creating series of random numbers with indexes of days obtained above
#3
s[dti.weekday == 2].sum() # sum of values in series whose indexex are wednesdays

#4 
s.resample('M').mean()#finding mean of each month by resampling for 1 month

#5
s.groupby(pd.Grouper(freq='4M')).idxmax()#grouping 4 months and computing the maximum value.
