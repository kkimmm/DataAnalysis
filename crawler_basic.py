
# coding: utf-8

# In[4]:

from bs4 import BeautifulSoup#Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构，
                              #每个节点都是Python对象。所有对象可以归纳为4种类型: Tag , NavigableString , BeautifulSoup , Comment


#1.Tag 
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'lxml')  #声明BeautifulSoup对象,使用lxml解析网页
find = soup.find('p')  #使用find方法查到第一个p标签
print("find's return type is: ", type(find))  #输出返回值类型
print("find's content is:", find)  #输出find获取的值
print("find's Tag Name is: ", find.name)  #输出标签的名字
print("find's Attribute(class) is :", find['class'])  #输出标签的class属性值


# In[6]:

#2.NavigableString

print('NavigableString is：', find.string)#NavigableString就是标签中的文本内容（不包含标签）获取方式如下：tag.string


# In[32]:

#3.BeautifulSoup & 4.comment
#BeautifulSoup对象表示一个文档的全部内容。支持遍历文档树和搜索文档树。

from bs4 import BeautifulSoup
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup,'lxml')
comment = soup.b.string #comment这个对象其实就是HTML和XML中的注释。
type (comment) 


# In[59]:

soup = BeautifulSoup(html_doc,'lxml')
print(soup.head) #查找head标签并打印
print(soup.title.text) #查找title标签内的内容然后打印
print(soup.title.string)#soup.title.string:表示现在titile的文本内容


# In[65]:

print(soup.body)#显示body标签下面的内容，也可以用.来叠加标签，例如下面的语句
print('\n' , soup.body.a , '\n')


# In[66]:

soup.get_text()#显示所有文本内容

