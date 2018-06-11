def hanoi(n,x,y,z):
    if n ==1:
        print(x, '->',z)
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从X移动到Y
        print(x,'->',z)#将最底下的一个盘子从X移动到Z
        hanoi(n-1,y,x,z)#将前n-1个盘子从Y移动到Z

n = int(input('请输入汉诺塔层数：'))
hanoi(n,'x','y','z')
