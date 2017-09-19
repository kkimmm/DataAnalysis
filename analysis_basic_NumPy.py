
# coding: utf-8

# In[2]:

import numpy as np
data1 = [6,75,8,0,1]
arr1 = np.array(data1)#列表转换为数组
arr1


# In[6]:

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
arr2


# In[11]:

np.zeros(10)


# In[13]:

np.zeros((2,10))


# In[17]:

np.empty((2,3,2)) #很多情况下会返回未初始化的垃圾值


# In[19]:

np.arange(15)


# In[6]:

arr1.dtype   #int型的
print(arr1.dtype)
float_arr = arr1.astype(np.float64)   #int型转换为float型
print(float_arr.dtype)
print(float_arr)


# In[10]:

numeric_strings = np.array(['2','1'])
numeric_strings.astype(float) #不写np.float64也能识别


# In[22]:

data3 = [[1,2],[1,2]]
arr3 = np.array(data3)
print(arr3)
print('\n',arr3 * arr3)#这里不是矩阵乘法，而是对应元素相乘
print('\n',arr3 - arr3)


# In[13]:

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[2])
print(arr2d[0,2])
print(arr2d[0][2])


# In[12]:

data4 = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
arr3d = np.array(data4)
print(arr3d[0])
old_value = arr3d[0].copy()
arr3d[0] = 42
print('\n---------\n',arr3d)
arr3d[0] = old_value
print('\n---------\n',arr3d)


# In[19]:

print(arr2d)
print('\n------------\n',arr2d[:2])
print('\n------------\n',arr2d[:2,:1])
print('\n------------\n',arr2d[1,:2])


# In[19]:

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data = np.random.randn(7,4)
print(names)
print('\n---------\n',data)
print('\n----------\n',names == 'Bob')
print('\n---------\n',data[names == 'Bob'])#显示第0行与第3行，即ture的行
print('\n---------\n',data[names == 'Bob',2:])
print('\n---------\n',data[names == 'Bob',3])


# In[8]:

arr5 = np.empty((8,4))
for i in range(8):
    arr5[i] = i
print(arr5)
print('\n---------\n',arr5[[4,2,0]])
print('\n---------\n',arr5[[-1,-2]])


# In[22]:

arr6 = np.arange(32).reshape((8,4))
print(arr6)
print('\n------\n',arr6[[1,5,7,2],[0,3,1,2]])
print('\n------\n',arr6[[1,5,7,2]][:,[0,3,1,2]])
print('\n------\n',arr6[np.ix_([1,5,7,2],[0,3,1,2])])


# In[30]:

arr7 = np.arange(15).reshape((3,5))
print(arr7)
print('\n----------\n',arr7.T)


# In[42]:

arr8 =  np.array([[1,2],[3,4]])
print(arr8)
print('\n---------\n',np.dot(arr8.T,arr8))#计算矩阵内积


# In[75]:

arr9 = np.arange(16).reshape((2,2,4))
print(arr9)
print('\n--------------\n',arr9.transpose((1,0,2)))
print('\n----------\n',arr9.shape)
print('\n----------\n',arr9[0][1][2])
print('\n--------------\n',arr9.swapaxes(1,2))


# In[86]:

arr10 = np.arange(32).reshape(2,4,4)
print('\n--------------\n',arr10)
print('\n----------\n',arr10.shape)
print('\n--------------\n',arr9.swapaxes(1,2))#swapaxes(d1,d2) 调换给定的两个维度 


# In[89]:

arr11 = np.arange(10)
print(arr11)
print('\n---------\n',np.sqrt(arr11))
print('\n---------\n',np.exp(arr11))


# In[104]:

x = np.random.randn(10)
y = np.random.randn(10)
print(x,'\n---------\n',y)
print('\n---------\n',np.maximum(x,y))


# In[107]:

get_ipython().magic('matplotlib inline')
points =  np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
print(xs)
import matplotlib.pyplot as plt
z = np.sqrt(xs ** 2 + ys ** 2)
print('\n--------\n',z)
plt.imshow(z,cmap = plt.cm.gray); plt.colorbar()


# In[111]:

xarr = np.array([1.1,1.2,1.3,1.4,1.5])
print(xarr)
yarr = np.array([2.1,2.2,2.3,2.4,2.5])
print(yarr)
cond = np.array([True,False,True,True,False])
result = [(x if c else y)
         for x,y,c in zip(xarr,yarr,cond)]
result


# In[114]:

result = np.where(cond,xarr,yarr)
result


# In[120]:

arr12 = np.random.randn(4,4)
print(arr12)
print('\n-------\n',np.where(arr12>0,2,arr12))
print('\n-------\n',np.where(arr12>0,2,0))


# In[125]:

arr13 = np.random.rand(5,4)
print(arr13.mean())
print('\n-----------\n',np.mean(arr13))
print('\n-----------\n',arr13.sum())


# In[141]:

arr14 = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(arr14)
print('\n-----------\n',arr14.sum(axis=1))#对行求和
print('\n-----------\n',arr14.sum(1))
print('\n-----------\n',arr14.sum(axis=0))
print('\n-----------\n',arr14.cumsum())
print('\n-----------\n',arr14.cumsum(0))


# In[170]:

arr15 = np.random.randn(100)
(arr15>0).sum()


# In[174]:

bools = np.array([False,False,True,False])
print(bools.any())
print(bools.all())


# In[202]:

arr16 = np.random.randn(10)
print(arr16)
print(arr16.sort())
print(arr16)


# In[206]:

arr17 = np.random.randn(4,5)
print(arr17)
arr17.sort(1)#只排第一行
print('\n----------\n',arr17)


# In[209]:

large_arr = np.random.randn(1000)
large_arr.sort()
large_arr[int(0.05*len(large_arr))]#计算5%分位数
#分位数：一堆数按照由小到大排序后分成n份，处于n-1个分割点位置的数即为分位数


# In[211]:

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
np.unique(names)


# In[214]:

ints = np.array([3,3,3,2,2,1,1,4,4])
np.unique(ints)


# In[217]:

values =np.array([6,0,0,3,2,5,6])
np.in1d(values,[2,3,6])


# In[220]:

arr16 = np.arange(10)
np.save('some_array',arr16)
np.load('some_array.npy')


# In[225]:

np.savez('array_archive.npz',a = arr16, b = arr16)
arch = np.load('array_archive.npz')
arch['b']


# In[229]:

x = np.array([[1,2],[3,4]])
y = np.array([[1,2],[3,4]])
x*y


# In[241]:

from numpy.linalg import inv,qr
X = np.random.randn(5,5)
mat = X.T.dot(X)
print(inv(mat))
print('\n----------\n',mat.dot(inv(mat)),'\n')
q,r = qr(mat)
print('\n',q,'\n----------\n',r)


# In[248]:

samples = np.random.normal(size = (4,4))
samples


# In[6]:

import random
position = 0
walk = [position]
step = 1000
for i in range(step):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)
print(position)
nsteps = 1000
draws = np.random.randint(0,2,size = nsteps)
steps = np.where(draws > 0,1,-1)
walk = steps.cumsum()
walk.min()
walk.max()

