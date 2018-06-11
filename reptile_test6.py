
# coding: utf-8

# In[19]:

import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
#print(soup.text)


# In[17]:

for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        time = news.select('.time')[0].text
        a = news.select('a')[0]['href']
        print(time,h2,a)


# In[55]:

import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/c/gat/2017-05-08/doc-ifyeycfp9371717.shtml')
res.encoding = 'utf-8'
#print(res.text)
soup = BeautifulSoup(res.text,'html.parser')
#print(soup.text)
#for basicInfo in soup.select('.basicInfo-item'):
#    print(basicInfo.text)
#soup.select('#artibodyTitle')[0].text
time = soup.select('.time-source')[0].contents[0].strip()#取得时间
time


# In[59]:

from datetime import datetime#转换时间格式
datetime.strptime(time,'%Y年%m月%d日%H:%M')


# In[62]:

soup.select('.time-source span a')[0].text#取得新闻来源


# In[75]:

article = []
for p in soup.select('#artibody p')[:-1]:
    #[:-1]是为了去掉最后一个p的东西
    article.append(p.text.strip())
print(article)
'@'.join(article)#合并文章


# In[76]:

[p.text.strip() for p in soup.select('#artibody p')[:-1]]#去上面的目的相同


# In[81]:

soup.select('.article-editor')[0].text.lstrip('责任编辑：')#取得编辑
#用lstrip('责任编辑：')从左边除去“责任编辑：”


# In[83]:

soup.select('.commentCount1')

