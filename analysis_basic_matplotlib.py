
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
from pylab import *
get_ipython().magic('matplotlib inline')


# In[2]:

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
from numpy.random import randn
plt.plot(randn(50).cumsum(),'k--')
ax1.hist(randn(1000),bins = 15 , color = 'k' ,alpha = 0.8)
ax2.scatter(np.arange(30),np.arange(30)+3*randn(30))


# In[3]:

fig,axes = plt.subplots(2,2,sharex = True,sharey=True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(randn(500),bins = 50,color = 'k',alpha = 0.5)
plt.subplots_adjust(wspace =0, hspace = 0)


# In[4]:

plt.plot(randn(30).cumsum(),'k*--')


# In[5]:

plot(randn(30).cumsum(),color = 'k',linestyle = 'dashed',marker = 'o')


# In[6]:

data = randn(30).cumsum()
plt.plot(data,'k--',label = 'Default')
plt.plot(data,'k-',drawstyle = 'steps-post',label = 'step-post')
plt.legend(loc='best')


# In[7]:

fig = plt.figure();
ax = fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum())
ticks = ax.set_xticks([0,250,500,750,1000])
labels = ax.set_xticklabels(['one','two','three','four','five'],
                           rotation =30,fontsize='small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')


# In[8]:

fig = plt.figure();
ax = fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum(),'k',label = 'one')
ax.plot(randn(1000).cumsum(),'k--',label ='two')
ax.plot(randn(1000).cumsum(),'k.',label = 'three')
ax.legend(loc = 'best')
ax.text(100,0,'Hello World!',
       family = 'monospace',fontsize = 10)


# In[9]:

from datetime import datetime
import pandas as pd
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
data = pd.read_csv('D:\\Github\\pydata-book-master\\ch08\\spx.csv',index_col = 0, parse_dates = True)
spx = data['SPX']
spx.plot(ax =ax,style = 'k-')
crisis_data = [
    (datetime(2007,10,11),'Peak of bull market'),
    (datetime(2008,3,12),'Bear Stearns Fails'),
    (datetime(2008,9,15),'Lehman Bankruptcy')
]

for data,label in crisis_data:
    ax.annotate(label,xy = (data,spx.asof(data)+50),
               xytext=(data,spx.asof(data)+200),
               arrowprops = dict(facecolor = 'black'),
               horizontalalignment = 'left',verticalalignment = 'top')

ax.set_xlim(['1/1/2007','1/1/2011'])
ax.set_ylim([600,1800])
plt.savefig('D:\\Python SaveFile\\1.png',dpi = 400,bbox_inches = 'tight')


# In[10]:

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
rect = plt.Rectangle((0.2,0.75),0.4,0.15,color = 'k',alpha = 0.3)
ax.add_patch(rect)
plt.savefig('D:\\Python SaveFile\\figpath.svg')
plt.savefig('D:\\Python SaveFile\\figpath.png',dpi = 400,bbox_inches = 'tight')


# In[11]:

from pandas import Series,DataFrame
s = Series(np.random.randn(10).cumsum(),index = np.arange(0,100,10))
print(s)
s.plot()


# In[12]:

df = DataFrame(np.random.randn(10,4).cumsum(0),
              columns = ['A','B','C','D'],
              index = np.arange(0,100,10))
print(df)
df.plot()


# In[13]:

fig,axes =plt.subplots(2,1)
data = Series(np.random.rand(16),index = list('abcdefghijklmnop'))
print(data)
data.plot(kind = 'bar',ax = axes[0],color = 'k',alpha = 0.7)
data.plot(kind= 'barh',ax = axes[1],color ='k',alpha=0.7)


# In[14]:

df = DataFrame(np.random.rand(6,4),
              index = ['one','two','three','four','five','six'],
              columns = pd.Index(['A','B','C','D'], name = 'Genus'))
print(df)
df.plot(kind = 'bar')


# In[15]:

df.plot(kind = 'bar',stacked = True,alpha = 0.5)


# In[16]:

tips = pd.read_csv('D:\\Github\\pydata-book-master\\ch08\\tips.csv')
party_counts = pd.crosstab(tips.day,tips.size)
party_counts


# In[19]:

party_counts = party_counts.ix[:,2:5]
party_pcts = party_counts.div(party_counts.sum(1).astype(float),axis = 0)
party_pcts


# In[20]:

comp1 = np.random.normal(0,1,size = 200) #N(0,1)
comp2 = np.random.normal(10,2,size = 200)#N(10,4)
values = Series(np.concatenate([comp1,comp2]))
values.hist(bins = 100,alpha = 0.3,color = 'k',normed = True)
values.plot(kind = 'kde',style = 'k--')


# In[23]:

macro = pd.read_csv('D:\\Github\\pydata-book-master\\ch08\\macrodata.csv')
data = macro[['cpi','m1','tbilrate','unemp']]
trans_data = np.log(data).diff().dropna()
trans_data


# In[29]:

plt.scatter(trans_data['m1'],trans_data['unemp'])
plt.title(' Changes in log%s vs. log%s ' %('m1','unemp'))


# In[30]:

pd.scatter_matrix(trans_data,diagonal = 'kde',c = 'k',alpha = 0.3)

