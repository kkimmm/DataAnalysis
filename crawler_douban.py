
# coding: utf-8

# In[1]:

import requests
from bs4 import BeautifulSoup
res = requests.get('https://movie.douban.com/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'lxml')
#print(soup.text)
#print(soup.select('.title'))

   


# In[17]:

a = soup.select('.title')
b = a[:10]
c = soup.select('.rating')[:10]
d = []
e = []

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



# In[18]:

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


# In[19]:

import csv  
def createListCSV():
    fileName='D:\\python CrawlerSaveFile\\2.csv' 
    dataList =e
    with open(fileName, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        for data in dataList:
            csvWriter.writerow(data)
        csvFile.close
        
g = createListCSV()


# In[12]:

a = []

for i in soup.select('.ui-slide-item '):
    a.append(i)

a = a[:10]
for j in a:
    print(j['data-actors'])

