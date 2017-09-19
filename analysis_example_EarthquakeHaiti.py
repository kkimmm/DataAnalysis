
# coding: utf-8

# In[5]:

import pandas as pd
data = pd.read_csv('D:\\Github\\pydata-book-master\\ch08\\Haiti.csv')
data


# In[6]:

data[['INCIDENT DATE','LATITUDE','LONGITUDE']][:10]


# In[7]:

data['CATEGORY']


# In[8]:

data.describe()


# In[9]:

data = data[(data.LATITUDE > 18)&(data.LATITUDE <20)&(data.LONGITUDE >-75)&(data.LONGITUDE < -70)&data.CATEGORY.notnull()]


# In[18]:

def to_cat_list(catstr):
    stripped = (x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]
def get_all_categories(cat_series):
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))
def get_english(cat):
    code,names = cat.split('.')
    if '|' in names:
        names = names.split('|')[1]
    return code,names.strip()


# In[19]:

get_english('2. Urgences logistiques | Vital Lines')


# In[20]:

all_cats = get_all_categories(data.CATEGORY)
english_mapping = dict(get_english(x) for x in all_cats)
english_mapping['2a']


# In[21]:

english_mapping['6c']


# In[26]:

import numpy as np
from pandas import Series,DataFrame
def get_code(seq):
    return [x.split('.') for x in seq if x]
all_codes = get_code(all_cats)
code_index = pd.Index(np.unique(all_codes))
dummy_frame = DataFrame(np.zeros((len(data),len(code_index))),index = data.index,columns = code_index)
dummy_frame.ix[:,:6]


# In[28]:

for row , cat in zip(data.index,data.CATEGORY):
    codes = get_code(to_cat_list(cat))
    dummy_frame.ix[row,codes] = 1
data = data.join(dummy_frame.add_prefix('category_'))
data.ix[:,10:15]


# In[ ]:



