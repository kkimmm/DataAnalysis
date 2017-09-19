
# coding: utf-8

# In[77]:

from pandas import Series,DataFrame
import numpy as np
import pandas as pd

df = DataFrame({'key1':['a','a','b','b','a'],
               'key2':['one','two','one','two','one'],
               'data1':np.random.randn(5),
               'data2':np.random.randn(5)})
df


# In[78]:

grouped = df['data1'].groupby(df['key1'])
grouped


# In[79]:

grouped.mean()


# In[80]:

means = df['data1'].groupby([df['key1'],df['key2']]).mean()
means


# In[81]:

means.unstack()


# In[82]:

states = np.array(['Ohio','California','California','Ohio','Ohio'])
years = np.array([2005,2005,2006,2005,2006])
df['data1'].groupby([states,years]).mean()


# In[83]:

df.groupby('key1').mean()


# In[84]:

df.groupby(['key1','key2']).mean()


# In[85]:

df.groupby(['key1','key2']).size()


# In[86]:

for name , group in df.groupby('key1'):
    print (name)
    print (group)


# In[87]:

for (k1,k2), group in df.groupby(['key1','key2']):
    print(k1,k2)
    print(group)


# In[88]:

pieces = dict(list(df.groupby('key1')))
pieces['b']


# In[89]:

df.dtypes


# In[90]:

grouped = df.groupby(df.dtypes,axis = 1)
dict(list(grouped))


# In[91]:

#df.groupby('key1')['data1']
#df.groupby('key2')['data2']
#df['data1'].groupby(df['key1'])
#df[['data2']].groupby(df['key1'])
df.groupby(['key1','key2'])[['data2']].mean()


# In[92]:

s_grouped = df.groupby(['key1','key2'])['data2']
s_grouped


# In[93]:

s_grouped.mean()


# In[94]:

people = DataFrame(np.random.randn(5,5),
                  columns = ['a','b','c','d','e'],
                  index = ['Joe','Steve','Wes','Jim','Travis'])
people.ix[2:3,['b','c']] = np.nan
people


# In[95]:

mapping = {'a':'red','b':'red','c':'blue','d':'blue','e':'red','f':'orange'}
by_columns = people.groupby(mapping,axis = 1)
by_columns.sum()


# In[96]:

map_series =Series(mapping)
map_series


# In[97]:

people.groupby(map_series,axis = 1).count()


# In[98]:

people.groupby(len).sum()


# In[99]:

key_list = ['one','one','one','two','two']
people.groupby([len,key_list]).count()


# In[100]:

columns = pd.MultiIndex.from_arrays([['US','US','US','JP','JP'],
                                    [1,3,5,1,3]],
                                   names = ['city','tenor'])
hier_df = DataFrame(np.random.randn(4,5),columns = columns)
hier_df


# In[101]:

hier_df.groupby(level = 'city',axis = 1).count()


# In[102]:

df


# In[103]:

grouped = df.groupby('key1')
grouped['data1'].quantile(0.2)


# In[104]:

def peak_to_peak(arr):
    return arr.max() - arr.min()
grouped.agg(peak_to_peak)


# In[105]:

grouped.describe()


# In[106]:

tips = pd.read_csv('D:\\Github\\pydata-book-master\\ch08\\tips.csv')
tips


# In[107]:

tips['tip_pct'] = tips['tip']/tips['total_bill']
tips


# In[108]:

grouped = tips.groupby(['sex','smoker'])
grouped_pct = grouped['tip_pct']
grouped_pct.agg('mean')


# In[109]:

grouped_pct.agg(['mean','std',peak_to_peak])


# In[110]:

grouped_pct.agg([('foo','mean'),('bar',np.std)])


# In[111]:

functions = ['count','mean','max']
result = grouped['tip_pct','total_bill'].agg(functions)
result


# In[112]:

result['tip_pct']


# In[113]:

ftuples = [('Durchschnitt','mean'),('Abweichung',np.var)]
grouped['tip_pct','total_bill'].agg(ftuples)


# In[114]:

grouped.agg({'tip':np.max,'size':'sum'})


# In[115]:

grouped.agg({'tip_pct':['min','max','mean','std'],
            'size':'sum'})


# In[116]:

tips.groupby(['sex','smoker'], as_index = False,).mean()


# In[117]:

df


# In[118]:

k1_means = df.groupby('key1').mean().add_prefix('mean_')
k1_means


# In[119]:

pd.merge(df,k1_means,left_on = 'key1',right_index = True)


# In[120]:

key = ['one','two','one','two','one']
people.groupby(key).mean()


# In[121]:

people.groupby(key).transform(np.mean)


# In[122]:

def demean(arr):
    return arr - arr.mean()
demeaned = people.groupby(key).transform(demean)
demeaned


# In[123]:

demeaned.groupby(key).mean()


# In[124]:

def top(df,n =5 , columns = 'tip_pct'):
    return df.sort_index(by = columns)[-n:]
top(tips,n=6)


# In[125]:

tips.groupby('smoker').apply(top)


# In[126]:

tips.groupby(['smoker','day']).apply(top, n=1,columns = 'total_bill')


# In[127]:

result = tips.groupby('smoker')['tip_pct'].describe()
result


# In[128]:

result.unstack('smoker')


# In[129]:

tips.groupby('smoker',group_keys = False).apply(top)


# In[130]:

frame = DataFrame({'data1':np.random.randn(1000),
                  'data2':np.random.randn(1000)})
factor = pd.cut(frame.data1,4)
factor[:10]


# In[131]:

def get_stats(group):
    return {'min':group.min(),
           'max':group.max(),
           'count':group.count(),
           'mean':group.mean()}
grouped = frame.data2.groupby(factor)
grouped.apply(get_stats).unstack()


# In[132]:

grouping = pd.qcut(frame.data1,10,labels = False)
grouped = frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()


# In[133]:

s =Series(np.random.randn(6))
s[::2] = np.nan
s


# In[134]:

s.fillna(s.mean())


# In[135]:

states = ['Ohio','New York' , 'Vermont', 'Florida','Oregon','Nevada','California','Idaho']
group_key = ['East']*4 +['West']*4
data = Series(np.random.randn(8),index = states)
data


# In[136]:

data[['Vermont','Nevada','Idaho']] = np.nan
data


# In[137]:

data.groupby(group_key).mean()


# In[138]:

fill_mean = lambda g :g.fillna(g.mean())
data.groupby(group_key).apply(fill_mean)


# In[139]:

fill_values = {'East':0.5,'West':-1}
fill_func = lambda g:g.fillna(fill_values[g.name])
data.groupby(group_key).apply(fill_func)


# In[140]:

suits = ['H','S','C','D']
card_val = (list(range(1,11)) + [10]*3)*4
base_names = ['A']  +list(range(2,11))+['J','K','Q']
cards = []
for suit in ['H','S','C','D']:
    cards.extend(str(num)+suit for num in base_names)
deck = Series(card_val,index = cards)


# In[141]:

deck


# In[142]:

def draw(deck, n=5):
    return deck.take(np.random.permutation(len(deck)))[:n]
draw(deck)


# In[143]:

get_suit = lambda card:card[-1]
deck.groupby(get_suit).apply(draw,n = 2)


# In[144]:

deck.groupby(get_suit,group_keys =False).apply(draw, n =2)


# In[145]:

df = DataFrame({'category':['a','a','a','a','b','b','b','b'],
               'data':np.random.randn(8),
               'weights':np.random.rand(8)})
df


# In[146]:

grouped = df.groupby('category')
get_wavg = lambda g:np.average(g['data'],weights = g['weights'])
grouped.apply(get_wavg)


# In[147]:

close_px = pd.read_csv('D:\\Github\\pydata-book-master\\ch09\\stock_px.csv',parse_dates= True,index_col = 0)
close_px


# In[148]:

close_px[-4:]


# In[149]:

rets = close_px.pct_change().dropna()
spx_corr = lambda x:x.corrwith(x['SPX'])
by_year = rets.groupby(lambda x :x.year)
by_year.apply(spx_corr)


# In[150]:

by_year.apply(lambda g : g['AAPL'].corr(g['MSFT']))


# In[151]:

import statsmodels.api as sm
def regress(data,yvar,xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1
    result = sm.OLS(Y,X).fit()
    return result.params
by_year.apply(regress,'AAPL',['SPX'])


# In[153]:

tips.pivot_table(index=['sex','smoker'])


# In[155]:

tips.pivot_table(['tip_pct','size'],index =['sex','day'],columns = 'smoker')


# In[156]:

tips.pivot_table(['tip_pct','size'],index = ['sex','day'],columns = 'smoker',margins = True)


# In[157]:

tips.pivot_table('tip_pct',index = ['sex','smoker'],columns = 'day',aggfunc = len,margins = True)


# In[158]:

tips.pivot_table('size',index = ['time','sex','smoker'],columns= 'day',aggfunc= 'sum',fill_value = 0)


# In[ ]:



