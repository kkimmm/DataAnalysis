
# coding: utf-8

# In[1]:

get_ipython().system('type D:\\\\Github\\\\pydata-book-master\\\\ch06\\\\ex1.csv')


# In[2]:

import pandas as pd
df = pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex1.csv')
df


# In[3]:

pd.read_table('D:\\Github\\pydata-book-master\\ch06\\ex1.csv',sep = ' , ')


# In[4]:

get_ipython().system('type D:\\\\Github\\\\pydata-book-master\\\\ch06\\\\ex2.csv')


# In[5]:

pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex2.csv',header = None)


# In[6]:

pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex2.csv',names = ['a','b','c','d','message'])


# In[7]:

names = ['a','b','c','d','message']
pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex2.csv',names = names, index_col = 'message')


# In[8]:

get_ipython().system('type D:\\\\Github\\\\pydata-book-master\\\\ch06\\\\csv_mindex.csv')


# In[9]:

parsed = pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\csv_mindex.csv',index_col = ['key1','key2'])
parsed


# In[10]:

list(open('D:\\Github\\pydata-book-master\\ch06\\ex3.txt'))


# In[11]:

result = pd.read_table('D:\\Github\\pydata-book-master\\ch06\\ex3.txt',sep = '\s+')
result


# In[12]:

get_ipython().system('type D:\\\\Github\\\\pydata-book-master\\\\ch06\\\\ex4.csv')


# In[13]:

pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex4.csv',skiprows = [0,2,3])


# In[14]:

get_ipython().system('type D:\\\\Github\\\\pydata-book-master\\\\ch06\\\\ex5.csv')


# In[15]:

result = pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex5.csv')
result


# In[16]:

pd.isnull(result)


# In[17]:

result = pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex5.csv',na_values = ['NULL'])
result


# In[18]:

sentinels = {'message':['foo','NA'],
            'something':['two']}
pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex5.csv',na_values = sentinels)


# In[19]:

result = pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex6.csv')
result


# In[20]:

pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex6.csv',nrows = 5)


# In[21]:

chunker = pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex6.csv',chunksize = 1000)
chunker


# In[22]:

from pandas import Series,DataFrame
chunker = pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex6.csv',chunksize = 1000)
tot = Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(),fill_value = 0)
tot = tot.order(ascending = False)
tot


# In[23]:

data = pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex5.csv')
data


# In[24]:

data.to_csv('C:\\Users\\MR.G\\Desktop\\out.csv')


# In[25]:

import sys
data.to_csv(sys.stdout,sep = '|')


# In[26]:

data.to_csv(sys.stdout,sep = '|',na_rep= 'Null')


# In[27]:

data.to_csv(sys.stdout,index = False,columns = ['a','b','c'])


# In[28]:

Series.from_csv('D:\\Github\\pydata-book-master\\ch06\\tseries.csv',parse_dates = True)


# In[29]:

get_ipython().system('type D:\\\\Github\\\\pydata-book-master\\\\ch06\\\\ex7.csv')


# In[30]:

import csv
f = open('D:\\Github\\pydata-book-master\\ch06\\ex7.csv')
reader = csv.reader(f)


# In[31]:

for line in reader:
    print (line)


# In[32]:

lines =list(csv.reader(open('D:\\Github\\pydata-book-master\\ch06\\ex7.csv')))
header,values = lines[0],lines[1:]
data_dict = {h: v for h, v in zip(header,zip(*values))}
data_dict


# In[33]:

obj = """
{"name":"Wes",
"places_lived":["United Stateds","Spain","Germany"],
"pet":null,
"siblings":[{"name":"Scott","age":25,"pet":"Zuko"},
            {"name":"Katie","age":33,"pet":"Cisco"}]
}
"""
import json
result = json.loads(obj)
result


# In[34]:

siblings = DataFrame(result['siblings'],columns = ['name','age','pet'])
siblings


# In[68]:

df1 = pd.read_csv('D:\\python CrawlerSaveFile\\1.csv',names =['star'])
df1


# In[69]:

df2 = pd.read_csv('D:\\Github\\2.csv',encoding="gb2312",names =['movie'])
df2


# In[73]:

result = pd.concat([df1, df2], axis=1, join='inner')
result


# In[75]:

frame = pd.read_csv('D:\\Github\\pydata-book-master\\ch06\\ex1.csv')
frame


# In[84]:

xls_file = pd.ExcelFile('D:\\Github\\1.xls')


# In[86]:

table = xls_file.parse('Sheet1')
table

