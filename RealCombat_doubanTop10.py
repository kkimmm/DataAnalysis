
# coding: utf-8

# In[6]:

import pandas as pd
import requests
from bs4 import BeautifulSoup
res = requests.get('https://movie.douban.com/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'lxml')


# In[7]:

a = soup.select('.title')
b = a[:10]
c = soup.select('.rating')[:10]
d = []
e = []
h = []


for move_name in b:
    str1 = move_name.text
    #print(str1)
    e.append([str1])
print(e)


for move_rate in c:
    str2 = move_rate.text
    print(str2)
    d.append([str2])        
print(d)
print(type(str2))
print(str2)

for i in soup.select('.ui-slide-item '):
    h.append(i)


str4 = ''
j = []  
for j in h[:10]:
    str3 = j['data-actors']
    print(str3)
   
    #str4 = list([str3])
    j.append([str3])


print(type(str3))    
print(j)


# In[25]:

#下面是保存成csv文档的方式（将一个二重列表[[],[]]写入到csv文件中）
import csv  
def createListCSV():
    fileName='D:\\python CrawlerSaveFile\\1.csv' 
    dataList =d
    with open(fileName, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        for data in dataList:
            csvWriter.writerow(data)
        csvFile.close
        
g = createListCSV()


# In[26]:

def createListCSV():
    fileName='D:\\python CrawlerSaveFile\\2.csv' 
    dataList =e
    with open(fileName, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        for data in dataList:
            csvWriter.writerow(data)
        csvFile.close
        
g = createListCSV()


# In[29]:

import pandas as pd
df1 = pd.read_csv('D:\\python CrawlerSaveFile\\1.csv',encoding="gb2312",names =['star'])
df1


# In[28]:

df2 = pd.read_csv('D:\\python CrawlerSaveFile\\2.csv',encoding="gb2312",names =['movie'])
df2


# In[30]:

result = pd.concat([df2, df1], axis=1, join='inner')
result
result.sort_index(by = 'star',ascending = False)


# In[33]:

pd.merge(df2,df1,how = 'outer',left_index = True,right_index = True)


# In[ ]:



