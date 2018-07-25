
# coding: utf-8

# In[35]:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model


# In[4]:

def get_data(filename):
    data = pd.read_csv(filename)#将.csv数据读入Pandas数据帧。
    X_parameter = [] #把Pandas数据帧转换为X_parameter和Y_parameter数据，并返回他们
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['square_feet'],data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append([float(single_price_value)])
    return X_parameter,Y_parameter
X , Y =get_data('D:\\Python SourceData\\input_data.csv')
print(X)
print(Y)


# In[5]:

#把X_parameter和Y_parameter拟合为线性回归模型。
#我们要写一个函数，输入为X_parameters、Y_parameter和你要预测的平方英尺值，返回a、b和预测出的价格值。 

#y = a+bx

def linear_model_main(X_parameters,Y_parameters,predict_value):     #这里使用的是scikit-learn机器学习算法包
    regr = linear_model.LinearRegression()#创建一个线性模型
    regr.fit(X_parameters,Y_parameters)#用X_parameters和Y_parameter训练它
    predict_outcome = regr.predict(predict_value)#predict_values 是需要预测的值
    predictions = {}   #创建一个名称为predictions的字典，存着a、b和预测值
    predictions['a'] = regr.intercept_  #调用截距赋值给a
    predictions['b'] = regr.coef_       #调用系数赋值给b
    predictions['predicted_value'] = predict_outcome
    return predictions  # 返回predictions字典为输出
result = linear_model_main(X,Y,700)
print('a = ',result['a'])
print('b = ',result['b'])
print('PredectedValue = ',result['predicted_value'])


# In[6]:

#写一个函数，输入为X_parameters和Y_parameters，显示出数据拟合的直线。
def show_linear_line(X_parameters,Y_parameters):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters,Y_parameters)
    plt.scatter(X_parameters,Y_parameters)#scatter画散点图
    plt.plot(X_parameters,regr.predict(X_parameters),color = 'red')
    #plt.xticks()#设置坐标轴刻度和大小
    #plt.yticks()#
    plt.show()
show_linear_line(X,Y)


# In[8]:

#尝试线性模型不成功的例子
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
def get_data(filename):
    data = pd.read_csv(filename)#将.csv数据读入Pandas数据帧。
    X_parameter = [] #把Pandas数据帧转换为X_parameter和Y_parameter数据，并返回他们
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['square_feet'],data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append([float(single_price_value)])
    return X_parameter,Y_parameter
X , Y =get_data('D:\\Python SourceData\\input_data1.csv')
print(X)
print(Y)

def linear_model_main(X_parameters,Y_parameters,predict_value):     #这里使用的是scikit-learn机器学习算法包
    regr = linear_model.LinearRegression()#创建一个线性模型
    regr.fit(X_parameters,Y_parameters)#用X_parameters和Y_parameter训练它
    predict_outcome = regr.predict(predict_value)#predict_values 是需要预测的值
    predictions = {}   #创建一个名称为predictions的字典，存着a、b和预测值
    predictions['a'] = regr.intercept_  #调用截距赋值给a
    predictions['b'] = regr.coef_       #调用系数赋值给b
    predictions['predicted_value'] = predict_outcome
    return predictions  # 返回predictions字典为输出
result = linear_model_main(X,Y,700)
print('a = ',result['a'])
print('b = ',result['b'])
print('PredectedValue = ',result['predicted_value'])
#写一个函数，输入为X_parameters和Y_parameters，显示出数据拟合的直线。
def show_linear_line(X_parameters,Y_parameters):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters,Y_parameters)
    plt.scatter(X_parameters,Y_parameters)#scatter画散点图
    plt.plot(X_parameters,regr.predict(X_parameters),color = 'red')
    #plt.xticks()#设置坐标轴刻度和大小
    #plt.yticks()#
    plt.show()
show_linear_line(X,Y)


# In[ ]:



