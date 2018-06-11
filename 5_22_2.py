def fac(n):#递归方法求阶乘
    if n ==1:
        return 1
    else:
        return n * fac(n-1)

number = int(input('请输入一个数：'))
result = fac(number)
print('%d 的阶乘是： %d' % (number,result))
