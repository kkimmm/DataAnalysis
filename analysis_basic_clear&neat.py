
# coding: utf-8

# In[1]:

from pandas import Series,DataFrame
import pandas as pd
df1 = DataFrame({'key':['b','b','a','c','a','a','b'],
                'data1':range(7)})
df2 = DataFrame({'key':['a','b','d'],
                'data2':range(3)})
df1


# In[2]:

df2


# In[4]:

pd.merge(df1,df2,on = 'key')


# In[5]:

df3 = DataFrame({'lkey':['b','b','a','c','a','a','b'],
                'data1':range(7)})
df4 = DataFrame({'rkey':['a','b','d'],
                'data2':range(3)})
pd.merge(df3,df4,left_on = 'lkey',right_on = 'rkey')


# In[6]:

pd.merge(df1,df2,how = 'outer')


# In[16]:

df1 = DataFrame({'key':['b','b','a','c','a','b'],
                'data1':range(6)})
df2 = DataFrame({'key':['a','b','a','b','d'],
                'data2':range(5)})
df1


# In[19]:

df2


# In[20]:

pd.merge(df1,df2,on = 'key',how = 'left')


# In[21]:

pd.merge(df1,df2,how = 'inner')


# In[22]:

pd.merge(df1,df2,how = 'inner')


# In[24]:

pd.merge(df1,df2,how = 'outer')


# In[28]:

left = DataFrame({'key1':['foo','foo','bar'],
                 'key2':['one','two','one'],
                 'lval':[1,2,3]})
right = DataFrame({'key1':['foo','foo','bar','bar'],
                  'key2':['one','one','one','two'],
                  'rval':[4,5,6,7]})
pd.merge(left,right,on = ['key1','key2'],how = 'outer')


# In[29]:

pd.merge(left,right,on = 'key1')


# In[30]:

pd.merge(left,right,on= 'key1',suffixes = ('_left','_right'))


# In[31]:

left1 = DataFrame({'key':['a','b','a','a','b','c'],
                 'value':range(6)})
right1 = DataFrame({'group_val':[3.5,7]},
                  index = ['a','b'])
left1


# In[32]:

right1


# In[34]:

pd.merge(left1,right1,left_on = 'key',right_index = True)


# In[36]:

pd.merge(left1,right1,left_on = 'key',right_index = True,how = 'outer')


# In[38]:

import numpy as np
lefth = DataFrame({'key1':['Ohio','Ohio','Ohio','Nevada','Nevada'],
                  'key2':[2000,2001,2002,2001,2002],
                  'data':np.arange(5)})
righth = DataFrame(np.arange(12).reshape((6,2)),
                  index = [['Nevada','Nevada','Ohio','Ohio','Ohio','Ohio'],
                          [2001,2000,2000,2000,2001,2002]],
                  columns = ['event1','event2'])
lefth


# In[39]:

righth


# In[40]:

pd.merge(lefth,righth,left_on = ['key1','key2'],right_index =True)


# In[41]:

pd.merge(lefth,righth,left_on = ['key1','key2'],
        right_index = True,how = 'outer')


# In[43]:

left2 = DataFrame([[1,2],[3,4],[5,6]],
                 index = ['a','c','e'],
                 columns = ['Ohio','Nevada'])
right2 = DataFrame([[7,8],[9,10],[11,12],[13,14]],
                  index = ['b','c','d','e'],
                 columns = ['Missouri','Alabama'])
left2  


# In[44]:

right2


# In[45]:

pd.merge(left2,right2,how = 'outer',left_index = True,right_index = True)


# In[47]:

left2.join(right2,how = 'outer')


# In[48]:

left1.join(right1,on = 'key')


# In[49]:

arr = np.arange(12).reshape((3,4))
arr


# In[51]:

np.concatenate([arr,arr],axis = 0)


# In[58]:

s1 = Series([0,1],index = ['a','b'])
s2 = Series([2,3,4],index = ['c','d','e'])
s3 = Series([5,6],index = ['f','g'])
pd.concat([s1,s2,s3])


# In[59]:

pd.concat([s1,s2,s3],axis = 1)


# In[60]:

s4  =pd.concat([s1*5,s3])
pd.concat([s1,s4],axis = 1)


# In[62]:

pd.concat([s1,s4],axis = 1,join = 'inner')


# In[64]:

pd.concat([s1,s4],axis = 1, join_axes = [['a','c','b','e']])


# In[68]:

result = pd.concat([s1,s1,s3],keys = ['one','two','three'])
result
#DataFrame(result)


# In[70]:

result.unstack()


# In[71]:

pd.concat([s1,s2,s3],axis = 1, keys = ['one','two','three'])


# In[73]:

df1 = DataFrame(np.arange(6).reshape((3,2)),
               index = ['a','b','c'],
               columns  =['one','two'])
df2 = DataFrame(5+np.arange(4).reshape((2,2)),
               index = ['a','c'],
               columns = ['three','four'])
pd.concat([df1,df2],axis = 1 , keys = ['level1','level2'])


# In[74]:

pd.concat({'level1':df1,'level2':df2},axis = 1)


# In[75]:

pd.concat([df1,df2],axis =1,keys = ['level1','level2'],names  =['upper','lower'])


# In[76]:

df1 = DataFrame(np.random.randn(3,4),
               columns = ['a','b','c','d'])
df2 = DataFrame(np.random.randn(2,3),
               columns = ['b','d','a'])
df1


# In[77]:

df2


# In[78]:

pd.concat([df1,df2],ignore_index = True)


# In[81]:

a = Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],
          index = ['f','e','d','c','b','a'])
b  = Series(np.arange(len(a),dtype = np.float64),
                     index = ['f','e','d','c','b','a'])
b[-1]  =np.nan
a


# In[82]:

b


# In[83]:

np.where(pd.isnull(a),b,a)


# In[84]:

b[:-2].combine_first(a[2:])


# In[86]:

df1 = DataFrame({'a':[1,np.nan,5,np.nan],
                'b':[np.nan,2,np.nan,6],
                'c':range(2,18,4)})

df2  = DataFrame({'a':[5,4,np.nan,3,7],
                 'b':[np.nan,3,4,6,8]})
df1


# In[87]:

df2


# In[88]:

df1.combine_first(df2)


# In[89]:

data = DataFrame(np.arange(6).reshape((2,3)),
                index = pd.Index(['Ohio','Colorado'],name = 'state'),
                columns = pd.Index(['one','two','three'],name = 'number'))
data


# In[91]:

result = data.stack()
result


# In[92]:

result.unstack()


# In[95]:

result.unstack('state')


# In[96]:

data = DataFrame({'k1':['one']*3+['two']*4,
                 'k2':[1,1,2,3,3,4,4]})
data


# In[97]:

data.duplicated()


# In[98]:

data.drop_duplicates()


# In[99]:

data['v1']  = range(7)
data.drop_duplicates(['k1'])


# In[100]:

data = DataFrame({'food':['bacon','pulled pork','bacon','Pastrami','corned beef','Bacon','pastrami','honey ham','nova lox'],
                 'cunces':[4,3,12,6,7.5,8,3,5,6]})
data


# In[101]:

meat_to_animal = {'bacon':'pig','pulled pork':'pig','pastrami':'cow','corned beef':'cow','honey ham':'pig','nova lox':'salmon'}


# In[105]:

data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
data


# In[106]:

data['food'].map(lambda x :meat_to_animal[x.lower()])


# In[107]:

data = Series([1,-999,2,-999,-1000,3])
data


# In[108]:

data.replace(-999,np.nan)


# In[109]:

data.replace([-999,-1000],np.nan)


# In[110]:

data.replace([-999,-1000],[np.nan,0])


# In[111]:

data.replace({-999:np.nan,-1000:0})


# In[112]:

data = DataFrame(np.arange(12).reshape((3,4)),
                index = ['Ohio','Colorado','New York'],
                columns = ['one','two','three','four'])
data


# In[113]:

data.index.map(str.upper)


# In[115]:

data.index = data.index.map(str.upper)
data


# In[116]:

data.rename(index = str.title,columns = str.upper)


# In[118]:

data.rename(index = {'OHIO':'INDIANA'},
           columns = {'three':'peekaboo'})


# In[119]:

_ = data.rename(index = {'OHIO':'INDIANA'},inplace = True)
data


# In[120]:

ages = [20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]
cats = pd.cut(ages,bins)
cats


# In[121]:

cats.labels


# In[124]:

pd.value_counts(cats)


# In[125]:

pd.cut(ages,[18,26,36,61,100],right = False)


# In[127]:

group_name = ['Youth','YongAdult','MiddleAged','Senior']
pd.cut(ages,bins,labels = group_name)


# In[131]:

data = np.random.rand(20)
cats = pd.cut(data,4,precision = 2)
pd.value_counts(cats)


# In[129]:

data = np.random.rand(1000)
cats = pd.qcut(data,4)
cats


# In[130]:

pd.value_counts(cats)


# In[132]:

pd.qcut(data,[0,0.1,0.5,0.9,1])


# In[137]:

np.random.seed(12345)
data = DataFrame(np.random.randn(1000,4))
data.describe()


# In[138]:

col = data[3]
col[np.abs(col)>3]


# In[140]:

data[(np.abs(data)>3).any(1)]


# In[141]:

data[np.abs(data)>3] = np.sign(data)*3
data.describe()


# In[142]:

df = DataFrame(np.arange(5*4).reshape(5,4))
sampler = np.random.permutation(5)
sampler


# In[143]:

df


# In[144]:

df.take(sampler)


# In[145]:

df.take(np.random.permutation(len(df))[:3])


# In[146]:

bag = np.array([5,7,-1,6,4])
sampler = np.random.randint(0,len(bag),size=10)
sampler


# In[148]:

draws = bag.take(sampler)
draws


# In[151]:

df = DataFrame({'key':['b','b','a','c','a','b'],
               'data1':range(6)})
df


# In[152]:

pd.get_dummies(df['key'])


# In[153]:

pd.get_dummies(df['data1'])


# In[156]:

dummies = pd.get_dummies(df['key'],prefix = 'key')
dummies


# In[157]:

df_with_dumy = df[['data1']].join(dummies)
df_with_dumy


# In[158]:

values = np.random.rand(10)
values


# In[162]:

bins = [0,0.2,0.4,0.6,0.8,1]
s= pd.cut(values,bins)
s.value_counts()


# In[163]:

pd.get_dummies(s)


# In[169]:

val = 'a,b, guido'
val.split(',')


# In[168]:

pieces = [x.strip() for x in val.split(',')]
pieces


# In[172]:

'm'.join(pieces)


# In[174]:

val.count('a')


# In[176]:

import re
text = 'foo bar\t baz \t qux'
re.split('\s+',text)


# In[178]:

regex = re.compile('\s+')
regex.split(text)


# In[179]:

regex.findall(text)


# In[183]:

data = {'Dave': 'dave@goole.com','Steve': 'steve@gmail.com','Rob' :'rob@gmail.com','Wes':np.nan}
data =  Series(data)
data


# In[184]:

data.isnull()


# In[185]:

data.str.contains('gmail')


# In[186]:

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9._]+\.[A-Z]{2,4}'
pattern


# In[191]:

s = data.str.findall(pattern,flags=re.IGNORECASE)
s


# In[188]:

matches = data.str.match(pattern,flags=re.IGNORECASE)
matches


# In[192]:

s.str.get(1)

