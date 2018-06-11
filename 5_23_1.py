number= int( input('请输入一个数') )
#这是递归调用实现斐波那契函数兔子问题
def fac1(n):
    if n<1:
        print('error')
        return -1
    if n ==1 or n ==2:
        return 1
    else:
        return fac1(n-1)+fac1(n-2)
         

result = fac1(number)
if result != -1:
    print('兔子总对数为:',result)
