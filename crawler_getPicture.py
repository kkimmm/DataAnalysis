
# coding: utf-8

# In[10]:

import requests #导入requests 模块
from bs4 import BeautifulSoup  #导入BeautifulSoup 模块
#r = requests.get("https://unsplash.com")


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}  
#给请求指定一个请求头来模拟chrome浏览器
web_url = 'https://unsplash.com'
r = requests.get(web_url, headers=headers) #像目标url地址发送get请求，返回一个response对象
all_a = BeautifulSoup(r.text, 'lxml').find_all('a', class_='cV68d')  #获取网页中的class为cV68d的所有a标签
for a in all_a: 
    img_str = a['style'] #a标签中完整的style字符串
    print(img_str)
    #print( img_str[img_str.index(' " ') + 1] : img_str.index ( ' " ',img_str[img_str.index('"') + 1  ]) ) #使用Python的切片功能截取双引号之间的内容

