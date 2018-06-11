import easygui as g
import sys

g.egdemo() #调用easygui的所有内置方法

g.msgbox('hello word')#显示hello word

g.msgbox('hello word','HELLO')#指定消息参数（hello word）和标题参数（HELLO）

g.msgbox('hello word','HELLO',ok_button = '确定！')#重写OK按钮内容


choice = ['yes','no']
reply = g.choicebox('hello , indian mi fans! are you ok?',choices = choice)
#选择

if g.ccbox('again ? ',choices = ('yes','no')):
    g.msgbox('its too late')#默认是pass
else:
    sys.exit(0)
#ccbox选择框，continue 或者cancel 并返回相应的值（continue返回1，cancel返回0）

g.buttonbox(msg='',title='',choice=('1','2','3'),image= None,root = None)
#buttonbox,返回点击按钮对应的值
#image 参数仅支持.gif格式的图像

g.buttonbox(msg='这是张图片',title='',choices=('yes','no'),image = 'C:\\Users\\MR.G\\Desktop\\test.gif')
#buttonbox中显示图片

g.enterbox(msg='请输入数据',title='',default='',strip = True，image = None,root = None)
#返回用户输入的数据，按照字符串格式返回，默认strip=True时去掉首位空格，如需要则设置strip = true


#。。。。。。
