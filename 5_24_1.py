def hanoi(n): #计算汉诺塔步数函数
    if n<1:
        print('error')
        return -1
    if n ==1:
        return 1
    elif n ==2:
        return 3
    else:
        return hanoi(n-1)+hanoi(n-1)+1

number = int(input('请输入一个数字：'))
result = hanoi(number)
if result !=-1:
    print(result)
