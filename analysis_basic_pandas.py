
# coding: utf-8

# In[6]:

import numpy as np
from pandas import Series,DataFrame
import pandas as pd
obj = Series([4,7,-5,3])
obj


# In[7]:

obj.values


# In[8]:

obj.index


# In[9]:

obj2 = Series([4,7,-5,3],index = ['b','b','a','c'])
obj2


# In[10]:

obj2.index


# In[11]:

obj2['a']


# In[12]:

obj2['b']


# In[13]:

obj2[['c','a']]


# In[14]:

obj2[obj2>0]


# In[15]:

obj2*2


# In[16]:

np.exp(obj2)


# In[17]:

obj2


# In[18]:

'b' in obj2


# In[19]:

sdata = {'Ohio':3500, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
obj3 = Series(sdata)
obj3


# In[20]:

states = ['California','Ohio','Oregon','Texas']
obj4 = Series(sdata, index = states)
obj4


# In[21]:

pd.isnull(obj4)


# In[22]:

pd.notnull(obj4)


# In[23]:

obj4.isnull()


# In[24]:

obj3+obj4


# In[25]:

obj4.name = 'population'
obj4.index.name = 'state'
obj4


# In[26]:

obj.index = ['Bob','Steve','Jeff','Ryan']
obj


# In[27]:

data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
       'year':[2000,2001,2002,2001,2002],
       'pop':[1.5,1.7,3.6,2.4,2.9]}
frame = DataFrame(data)
frame


# In[28]:

DataFrame(data,columns = ['year','state','pop'])


# In[29]:

frame2 = DataFrame(data,columns = ['year','state','pop','debt'],
                  index = ['one','two','three','four','five'])
frame2


# In[30]:

frame2.columns


# In[31]:

frame2['state']


# In[32]:

frame2.year


# In[33]:

frame2.ix['three']


# In[34]:

frame2['debt'] = 16.5
frame2


# In[35]:

frame2['debt'] = np.arange(5)
frame2


# In[36]:

val = Series([-1.2,-1.5,-1.7], index = ['two','four','five'])
frame2['debt'] = val
frame2


# In[37]:

frame2['eastern'] = frame2.state =='Ohio'
frame2


# In[38]:

del frame2['eastern']
frame2.columns


# In[39]:

pop = {'Nevada':{2001:2.4 , 2002:2.9},
      'Ohio':{2000:1.5 , 2001:1.7 , 2002:3.6}}
frame3 = DataFrame(pop)
frame3


# In[40]:

frame3.T


# In[41]:

DataFrame(pop,index = [2001,2002,2003])


# In[42]:

pdata = {'Ohio':frame3['Ohio'][:-1],
        'Nevada':frame3['Nevada'][:2]}
DataFrame(pdata)


# In[43]:

frame3.index.name = 'year' ;
frame3.columns.name = 'state'
frame3


# In[44]:

frame3.values


# In[45]:

frame2.values


# In[46]:

obj = Series(range(3),index = ['a','b','c'])
index = obj.index
index


# In[47]:

index[1:]


# In[48]:

index = pd.Index(np.arange(3))
obj2 = Series([1.5,-2.5,0],index = index)
obj2.index is index


# In[49]:

frame3


# In[50]:

'Ohio' in frame3.columns


# In[51]:

obj = Series([4.5,7.2,-5.3,3.6],index = ['d','b','a','c'])
obj


# In[52]:

obj2 = obj.reindex(['a','b','c','d','e'])
obj2


# In[53]:

obj.reindex(['a','b','c','d','e'],fill_value = 0)


# In[54]:

obj3 = Series(['blue','purple','yellow'],index = [0,2,4])
obj3.reindex(range(6),method = 'ffill')


# In[55]:

frame = DataFrame(np.arange(9).reshape((3,3)),index = ['a','b','c'],columns = ['Ohio','Texas','California'])
frame


# In[57]:

frame2 = frame.reindex(['a','b','c','d'])
frame2


# In[59]:

state = ['Texas','Utah','California']
frame.reindex(columns = states)


# In[60]:

frame.reindex(index = ['a','b','c','d'],method = 'ffill',columns = states)


# In[61]:

frame.ix[['a','b','c','d'],states]


# In[63]:

obj5 = Series(np.arange(5),index = ['a','b','c','d','e'])
new_obj5 =obj5.drop('c')
new_obj5


# In[64]:

obj5.drop(['d','c'])


# In[65]:

data = DataFrame(np.arange(16).reshape((4,4)),
                index = ['Ohio','Colorado','Utah','New York'],
                columns = ['one','two','three','four'])
data.drop(['Colorado','Ohio'])


# In[66]:

data.drop('two',axis = 1)


# In[67]:

obj6 =Series(np.arange(4),index = ['a','b','c','d'])
obj6['b']


# In[68]:

obj6[1]


# In[70]:

obj6[['b','a']]


# In[73]:

obj6['b':]


# In[74]:

data


# In[75]:

data['two']


# In[76]:

data[:2]


# In[77]:

data[data['three'] > 5]


# In[78]:

data < 5


# In[79]:

data[data<5] = 0
data


# In[80]:

data.ix['Colorado',['two','three']]


# In[81]:

data.ix[['Colorado','Utah'],[3,0,1]]


# In[82]:

data.ix[2]


# In[83]:

data.ix[data.three > 5 ,:3]


# In[84]:

s1 = Series([7.3,-2.5,3.4,1.5],index = ['a','c','d','e'])
s2 = Series([-2.1,3.6,-1.5, 4, 3.1],index = ['a','c','e','f','g'])
s1


# In[86]:

s2


# In[87]:

s1+s2


# In[88]:

df1 = DataFrame(np.arange(9).reshape((3,3)),
               columns = list('bcd'),
               index = ['Ohio','Texas','Colorado'])
df2 = DataFrame(np.arange(12).reshape((4,3)),
               columns = list('bde'),
               index = ['Utah','Ohio','Texas','Oregon'])
df1


# In[89]:

df2


# In[90]:

df1+df2


# In[91]:

df1.add(df2,fill_value = 0)


# In[92]:

df1.reindex(columns = df2.columns,fill_value = 0)


# In[93]:

arr = np.arange(12).reshape((3,4))
arr


# In[94]:

arr[0]


# In[95]:

arr - arr[0]


# In[96]:

frame3 = DataFrame(np.arange(12).reshape((4,3)),
                  columns = list('bde'),
                  index = ['Utah','Ohio','Texas','Oregon'])
series = frame3.ix[0]
frame3


# In[97]:

series


# In[98]:

frame3 - series


# In[99]:

series2 = Series(range(3),index = ['b','e','f'])
frame3 + series2


# In[100]:

series3 = frame3['d']
frame3


# In[102]:

series3


# In[106]:

frame4 = frame3.sub(series3,axis = 0)
frame4


# In[107]:

np.abs(frame4)


# In[112]:

print(frame3,'\n----------')
f = lambda x: x.max() - x.min()
frame3.apply(f)


# In[110]:

def f(x):
    return Series ([x.min(),x.max()],
                  index = ['min','max'])
frame3.apply(f)


# In[114]:

obj3 = Series(range(4),index = ['d','a','b','c'])
obj3.sort_index()


# In[120]:

frame5 = DataFrame(np.arange(8).reshape((2,4)),
                  index = ['three','one'],
                  columns = ['d','a','b','c'])
frame5.sort_index()


# In[123]:

frame5.sort_index(axis =0)


# In[122]:

frame5.sort_index(axis = 1, ascending = False)


# In[124]:

obj4 = Series([4,7,-3,2])
obj4.order()


# In[131]:

obj5 = Series([4,np.nan,7,np.nan,-3,2])
#obj5.sort_index()
obj5.order()


# In[132]:

frame6 = DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
frame6


# In[135]:

frame6.sort_index(by = 'b')


# In[137]:

frame6.sort_index(by = ['a','b'])


# In[138]:

obj6 = Series([7,-5,7,4,2,0,4])
obj6.rank()


# In[139]:

obj6.rank(method = 'first')


# In[140]:

obj7 = Series(range(5),index = ['a','a','b','b','c'])
obj7


# In[141]:

obj7.index.is_unique


# In[142]:

obj7['a']


# In[143]:

obj7['c']


# In[144]:

df = DataFrame([[1.4,np.nan],[7.1,-4.5],
                [np.nan,np.nan],[0.75,-1.3]],
              index = ['a','b','c','d'],
              columns = ['one','two'])
df


# In[145]:

df.sum()


# In[146]:

df.sum(axis = 1)


# In[147]:

df.mean()


# In[148]:

df.idxmax()


# In[149]:

df.describe()


# In[151]:

obj8 = Series(['c','a','d','a','a','b','b','c','c'])
u = obj8.unique()
u


# In[155]:

obj8.value_counts()


# In[157]:

pd.value_counts(obj8.values,sort = False)


# In[158]:

mask = obj8.isin(['b','c'])
mask


# In[160]:

obj8[mask]


# In[161]:

data = DataFrame({'Qu1':[1,3,4,3,4],
                 'Qu2':[2,3,1,2,3],
                 'Qu3':[1,5,2,4,4]})
data


# In[162]:

result = data.apply(pd.value_counts).fillna(0)
result


# In[163]:

string_data = Series(['aardvark','artichoke',np.nan,'avocado'])
string_data


# In[164]:

string_data.isnull()


# In[165]:

string_data[0] = None
string_data.isnull()


# In[166]:

from numpy import nan as NA
data = Series([1,NA,3.5,NA,7])
data.dropna()


# In[167]:

data[data.notnull()]


# In[168]:

data = DataFrame([[1.,6.5,3.],[1.,NA,NA],
                 [NA,NA,NA],[NA,6.5,3.]])
cleaned = data.dropna()
data


# In[169]:

cleaned


# In[170]:

data.dropna(how = 'all')


# In[174]:

data[4] = NA
data


# In[173]:

data.dropna(axis = 1,how = 'all')


# In[175]:

df = DataFrame(np.random.rand(7,3))
df.ix[:4,1] = NA;df.ix[:2,2] = NA
df


# In[183]:

df.dropna(thresh = 2)


# In[184]:

df.fillna(0)


# In[185]:

df.fillna({1:0.5,3:-1})


# In[188]:

_ = df.fillna(0,inplace = True)
df


# In[189]:

df = DataFrame(np.random.randn(6,3))
df.ix[2:,1] = NA;df.ix[4:,2] =NA
df


# In[192]:

df.fillna(method = 'ffill')


# In[193]:

data = Series([1.,NA,3.5,NA,7])
data.fillna(data.mean())


# In[195]:

data = Series(np.random.randn(10),
             index = [['a','a','a','b','b','b','c','c','d','d'],
                     [1,2,3,1,2,3,1,2,2,3]])
data


# In[196]:

data.index


# In[197]:

data['b']


# In[198]:

data['b':'c']


# In[199]:

data[:,2]


# In[200]:

data.unstack()


# In[201]:

data.unstack().stack()


# In[202]:

frame = DataFrame(np.arange(12).reshape((4,3)),
                 index = [['a','a','b','b'],[1,2,1,2]],
                 columns = [['Ohio','Ohio','Colorado'],
                           ['Green','Red','Green']])
frame


# In[203]:

frame.index.names = ['key1','key2']
frame.columns.names = ['state','color']
frame


# In[204]:

frame['Ohio']


# In[205]:

frame.swaplevel('key1','key2')


# In[206]:

frame.sortlevel(1)


# In[207]:

frame.swaplevel(0,1).sortlevel(0)


# In[210]:

frame


# In[211]:

frame.sum(level = 'key2')


# In[213]:

frame.sum(level = 'color',axis = 1)

