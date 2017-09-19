
# coding: utf-8

# In[1]:

from datetime import datetime
now = datetime.now()
now


# In[2]:

now.year,now.month,now.day


# In[3]:

delta = datetime(2017,5,20) - datetime(2017,5,19,8,15)
delta


# In[4]:

delta.days


# In[5]:

delta.seconds


# In[6]:

from datetime import timedelta
start = datetime(2017,1,7)
start + timedelta(12)


# In[7]:

start - 2*timedelta(12)


# In[8]:

stamp = datetime(2017,1,3)
str(stamp)


# In[9]:

stamp.strftime('%Y-%m-%d')


# In[10]:

value = '2017-01-03'
datetime.strptime(value,'%Y-%m-%d')


# In[11]:

datestrs = ['7/6/2017','8/6/2017']
[datetime.strptime(x,'%m/%d/%Y') for x in datestrs]


# In[12]:

from dateutil.parser import parse
parse('2011-01-03')


# In[13]:

parse('Jan 31,1997 10:45 PM')


# In[14]:

parse('6/12/2017',dayfirst = True)


# In[15]:

datestrs


# In[16]:

import pandas as pd
pd.to_datetime(datestrs)


# In[17]:

idx = pd.to_datetime(datestrs + [None])
idx


# In[18]:

idx[2]


# In[19]:

pd.isnull(idx)


# In[20]:

from datetime import datetime
from pandas import Series,DataFrame
import numpy as np
dates = [datetime(2017,1,2),datetime(2017,1,5),datetime(2017,1,7),datetime(2017,1,8),datetime(2017,1,10),datetime(2017,1,12)]
ts = Series(np.random.randn(6),index = dates)
ts


# In[21]:

type(ts)


# In[22]:

ts.index


# In[23]:

ts+ts[::2]


# In[24]:

ts.index.dtype


# In[25]:

stamp = ts.index[0]
stamp


# In[26]:

stamp = ts.index[2]
ts[stamp]


# In[27]:

ts['1/10/2017']


# In[28]:

longer_str = Series(np.random.randn(1000),index = pd.date_range('1/1/2017',periods = 1000))
longer_str


# In[29]:

longer_str['2017']


# In[30]:

longer_str['2017-05']


# In[31]:

ts[datetime(2017,1,7)]


# In[32]:

ts


# In[33]:

ts['1/6/2017':'1/12/2017']


# In[34]:

ts.truncate(after = '1/9/2017')


# In[35]:

dates = pd.date_range('1/1/2017',periods = 100,freq = 'W-WED')
long_df = DataFrame(np.random.randn(100,4),
                   index = dates,
                   columns = ['Colorado','Texas','New York','Ohio'])
long_df


# In[36]:

long_df.ix['5-2017']


# In[37]:

dates = pd.DataFrame(['1/1/2017','1/2/2017','1/2/2017','1/2/2017','1/3/2017'])
dup_ts = Series(np.arange(5),index = dates)
dup_ts


# In[38]:

dup_ts.index.is_unique


# In[39]:

grouped = dup_ts.groupby(level = 0)
grouped.count()


# In[40]:

ts


# In[41]:

ts.resample('D')


# In[42]:

ts.resample('D').mean()   # 填充空日期


# In[43]:

index = pd.date_range('4/1/2017','6/1/2017')
index


# In[44]:

pd.date_range(start = '4/1/2017',periods = 20)


# In[45]:

pd.date_range(end = '6/1/2017',periods = 20)


# In[46]:

pd.date_range('1/1/2017','12/1/2017',freq = 'BM')


# In[47]:

pd.date_range('5/2/2017 12:56:31',periods = 5)


# In[48]:

pd.date_range('5/2/2017 12:56:31',periods = 5, normalize = True)


# In[49]:

from pandas.tseries.offsets import Hour,Minute
hour = Hour()
hour


# In[50]:

four_hours = Hour(4)
four_hours


# In[51]:

pd.date_range('1/1/2017','1/3/2017 23:59',freq = '4h')


# In[52]:

Hour(2)+Minute(30)


# In[53]:

pd.date_range('1/1/2017',periods = 10,freq = '1h30min')


# In[54]:

rng = pd.date_range('1/1/2017','9/1/2017',freq = 'WOM-3FRI')
list(rng)


# In[55]:

ts = Series(np.random.randn(4),
           index = pd.date_range('1/1/2017',periods = 4,freq = 'M'))
ts


# In[56]:

ts.shift(2)


# In[57]:

ts.shift(-2)


# In[58]:

ts/ts.shift(1) - 1


# In[59]:

ts.shift(2,freq = 'M')


# In[60]:

ts


# In[61]:

ts.shift(3,freq = 'D')


# In[62]:

from pandas.tseries.offsets import Day,MonthEnd
now = datetime(2017,11,17)
now + 3*Day()


# In[63]:

now + MonthEnd()


# In[64]:

now + MonthEnd(2)


# In[65]:

offset = MonthEnd()
offset.rollforward(now)


# In[66]:

offset.rollback(now)


# In[67]:

ts = Series(np.random.randn(20),
           index = pd.date_range('1/15/2017',periods = 20,freq = '4d'))
ts


# In[68]:

ts.groupby(offset.rollforward).mean()


# In[69]:

ts.resample('M',how = 'mean')


# In[70]:

import pytz
pytz.common_timezones[-5:]


# In[71]:

rng = pd.date_range('3/9/2017 9:30',periods = 6 , freq = 'D')
ts = Series(np.random.randn(len(rng)),index = rng)
print(ts.index.tz)


# In[72]:

pd.date_range('3/9/2017 9:30',periods = 10, freq = 'D',tz = 'UTC')


# In[73]:

ts


# In[74]:

ts_utc = ts.tz_localize('UTC')
ts_utc


# In[75]:

ts_utc.index


# In[77]:

ts_eastern = ts.tz_localize('US/Eastern')
ts_eastern.tz_convert('UTC')


# In[78]:

p = pd.Period(2017,freq = 'A-DEC')
p


# In[79]:

p+5


# In[82]:

pd.Period('2018',freq = 'A-DEC') -p


# In[83]:

rng = pd.period_range('1/1/2017','6/30/2017',freq = 'M')
rng


# In[84]:

Series(np.random.randn(6),index = rng)


# In[85]:

p = pd.Period('2017',freq = 'A-DEC')
p.asfreq('M',how = 'start')


# In[87]:

p= pd.Period('2017',freq = 'A-JUN')
p.asfreq('M','start')


# In[ ]:



