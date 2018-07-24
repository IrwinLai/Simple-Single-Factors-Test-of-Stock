# for the factors can get directly in financial statements
# python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import floor

def pur(data,factor,stop):   # the function to purchase the stock. stop is dictionary of the factors, which are suspended.
    purdic = {}
    
    threshold80 = data[factor].quantile(0.8)   # get the 80% of the factor
    threshold60 = data[factor].quantile(0.6)
    threshold40 = data[factor].quantile(0.4)
    threshold20 = data[factor].quantile(0.2)
    
    tem1 = {}
    tem1.update(stop.get('0-20'))    # purchase the suspended stock again, for actually they were not sold last month.
    temweight = sum(list(stop.get('0-20').values()))   # the total weight of suspended stock
    target = data.loc[ data[factor] > threshold80 ]    # add the top 20% stock
    for i in range(len(target)):
        tem1.update({target.iloc[[i][0]][0]:(1-temweight)/len(target)})   # purchase the stocks with the same weight
    purdic.update({'0-20':tem1})
    temweight = 0
    
    tem1 = {}
    tem1.update(stop.get('20-40'))
    temweight = sum(list(stop.get('20-40').values()))
    target = data.loc[(data[factor] > threshold60) & (data[factor] < threshold80)]
    for i in range(len(target)):
        tem1.update({target.iloc[[i][0]][0]:(1-temweight)/len(target)})
    purdic.update({'20-40':tem1})
    temweight = 0

    tem1 = {}
    tem1.update(stop.get('40-60'))
    temweight = sum(list(stop.get('40-60').values()))
    target = data.loc[(data[factor] > threshold40) & (data[factor] < threshold60)]
    for i in range(len(target)):
        tem1.update({target.iloc[[i][0]][0]:(1-temweight)/len(target)})
    purdic.update({'40-60':tem1})
    temweight = 0
    
    tem1 = {}
    tem1.update(stop.get('60-80'))
    temweight = sum(list(stop.get('60-80').values()))
    target = data.loc[(data[factor] > threshold20) & (data[factor] < threshold40)]
    for i in range(len(target)):
        tem1.update({target.iloc[[i][0]][0]:(1-temweight)/len(target)})
    purdic.update({'60-80':tem1})
    temweight = 0

    tem1 = {}
    tem1.update(stop.get('80-100'))
    temweight = sum(list(stop.get('80-100').values()))
    target = data.loc[data[factor] < threshold20]
    for i in range(len(target)):
        tem1.update({target.iloc[[i][0]][0]:(1-temweight)/len(target)})
    purdic.update({'80-100':tem1})
    temweight = 0
    return purdic
    
 
 def earn(date,purdic,capital,data,account,end):  # the function to calculate the earning 
    allstock = data.loc[data.index == date]  # account is the available money, end=1 means it is the end of the month
    stocklist = list(allstock['code'])
    k = 0
    stop = {'0-20':{},'20-40':{},'40-60':{},'60-80':{},'80-100':{}}
    for rank in list(purdic.keys()):
        hold = list(purdic.get(rank).keys())   # the stock we hold now
        totalchange = 0
        dailyearning = 0
        amount = len(hold)
        for i in range(amount):  
            weight = purdic.get(rank)[hold[i]]
            if hold[i] in stocklist:   # if the stock is not suspanded, then get the daily change
                change = allstock.loc[allstock['code'] == hold[i],'change'][0]
            else:    # if the stock is suspanded
                change = 0
                if end == 1:   # add it into stop dictionary
                    stop.get(rank).update({hold[i]:weight})
            dailyearning += round(account[k] * change * weight,2)   # total daily earning
        capital.get(rank).update({date:dailyearning})
        account[k] += dailyearning
        if account[k] <= 0:   # close the account, if the money is used up
            account[k] = 0
        k += 1
        
    return capital,stop
    
    
data = pd.read_csv("2010-2018mcap.csv",dtype={'code':str})   # read the data
data = data.loc[data['date'] > '2011']
del data['Unnamed: 0']
df = pd.read_csv('2010-2018market,zyyx.csv', index_col = 'date',dtype={'code':str})
tradedate = pd.read_csv('2011-2018tradedate.csv')   # the date when stock market open
del df['Unnamed: 0']

# initialize
# 'pub' is the deadline financial statement, 'sta' is the type of the statement and '1001' means the statement for the first season.
# actually in this area, using loop is a better choice.
pub = ['2010-11-01','2011-05-01','2011-09-01','2011-11-01','2012-05-01','2012-09-01','2012-11-01','2013-05-01','2013-09-01','2013-11-01','2014-05-01','2014-09-01','2014-11-01',\
       '2015-05-01','2015-09-01','2015-11-01','2016-05-01','2016-09-01','2016-11-01','2017-05-01','2017-09-01','2017-11-01','2018-05-01','2018-05-02']
sta = ['1003','1004','1002','1003','1004','1002','1003','1004','1002','1003','1004','1002','1003','1004','1002','1003','1004','1002','1003','1004','1002','1003','1004','1002']
capital = {'0-20':{},'20-40':{},'40-60':{},'60-80':{},'80-100':{}}
initial = 100000000
account = [initial/5 for i in range(5)]
factor = 'mcap'
purdic = {}
stop = {'0-20':{},'20-40':{},'40-60':{},'60-80':{},'80-100':{}}

for i in range(1,len(pub)-1):
    end = 0
    # the data between two deadline fo statement
    temdata = data.loc[(data['date']>pub[i-1]) & (data['date']<pub[i])]
    temcode  = list(temdata.code.unique())
    aimdata = pd.DataFrame()
    for w in range(len(temcode)):
        tt = temdata.loc[temdata['code'] == temcode[w]]
        tt.sort_values(by=['date'],ascending = False)
        aimdata = aimdata.append(tt.head(1))
    purdic = pur(aimdata,factor,stop)  # purchase
    temdate = list(tradedate.loc[(tradedate['0']>pub[i]) & (tradedate['0']<=pub[i+1])]['0'])
    for j in range(len(temdate)):
        end = 1 if temdate[j]==pub[i+1] else 0  # is it the end of the month?
        capital,stop = earn(temdate[j],purdic,capital,df,account,end)  # earning
        
# plot the pichture
plt.subplots(figsize = (16,5.5))
tem = pd.DataFrame(capital).cumsum()
tem.index = pd.to_datetime(tem.index)
for i in capital.keys():
    #tem[i] = tem[i]/(initial/5) + 1  # standardiez the earning
    tem[i].plot(label = i)
plt.legend(loc='best')
plt.show()