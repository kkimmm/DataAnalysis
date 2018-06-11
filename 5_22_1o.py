print('请输入一个数字：') #非递归阶乘
n = int( input() )
a = range(1,n+1)
b =1
for i in a:
    b = b*i
print(n,'的阶乘为：',b)

