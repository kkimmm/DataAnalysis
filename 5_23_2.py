number = int(input('请输入一个数字'))
#这是一个迭代（非递归）函数实现的斐波那契函数兔子问题
def fac2(n):
    n1 = 1
    n2 = 1
    n3 = 2
    
    if n==1:
        print('兔子总对数为',1)
        return -1
    elif n==2:
        print('兔子总对数为',1)
        return -1

        
    while (n-2)>0:
        n3 = n2+ n1
        n1 = n2
        n2 = n3
        n = n-1

    return n3

result = fac2(number)
if result !=-1:
    print('兔子对总数为：',result)
    
