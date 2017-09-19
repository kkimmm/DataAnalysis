
# coding: utf-8

# In[81]:

from pandas import Series,DataFrame
import pandas as pd
data = pd.read_csv('D:\\Python SourceData\\Yunnan_201501.csv') 
data


# In[82]:

data.set_index('城市', inplace=True)
data1= DataFrame(data,columns = ['监测点','时间','AQI','PM2.5','PM10','CO','NO2','O3','SO2','质量等级'])
data2 = data1.ix['楚雄州'][:40]
data2
#states = ['时间','AQI','PM2.5']
#data2.reindex(columns = states)


# In[83]:

data2.set_index('监测点', inplace=True)
data3 = DataFrame(data2,columns = ['时间','AQI','PM2.5','PM10','CO','NO2','O3','SO2','质量等级'])
data3


# In[84]:

data4 = data3.drop(['市经济开发区','州环境监测站'])
data4


# In[87]:

data4.set_index('时间', inplace=True)
data5 = DataFrame(data4,columns = ['AQI','PM2.5','PM10','CO','NO2','O3','SO2','质量等级','城市'])
data5


# In[78]:

data5.describe()


# In[79]:

data5.AQI.corr(data5.NO2 )


# In[ ]:



