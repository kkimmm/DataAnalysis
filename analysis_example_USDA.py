
# coding: utf-8

# In[1]:

import json
db = json.load(open('D:\\Github\\pydata-book-master\\ch07\\foods-2011-10-03.json'))
len(db)


# In[2]:

db[0].keys()


# In[3]:

db[0]['nutrients'][0]


# In[5]:

from pandas import Series,DataFrame
nutrients = DataFrame(db[0]['nutrients'])
nutrients[:7]


# In[6]:

info_keys = ['description','group','id','manufacturer']
info = DataFrame(db,columns = info_keys)
info[:5]


# In[7]:

info


# In[9]:

import pandas as pd
pd.value_counts(info.group)[:10]


# In[14]:

nutrients = []
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id']= rec['id']
    nutrients.append(fnuts)
    
nutrients = pd.concat(nutrients,ignore_index = True)


# In[15]:

nutrients.duplicated().sum()


# In[16]:

nutrients = nutrients.drop_duplicates()


# In[17]:

col_mapping = {'description':'food',
              'group':'fgroup'}
info = info.rename(columns = col_mapping,copy = False)
info


# In[19]:

col_mapping = {'description':'nutrient',
              'group':'nutgroup'}
nutrients = nutrients.rename(columns = col_mapping,copy = False)
nutrients


# In[20]:

ndata = pd.merge(nutrients,info, on = 'id',how = 'outer')
ndata


# In[21]:

ndata.ix[30000]


# In[26]:

result = ndata.groupby(['nutrient','fgroup'])['value'].quantile(0.5)
#result['Zinc,Zn'].order().plot(kind = 'barh')

