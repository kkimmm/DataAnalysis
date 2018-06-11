import random
secret=random.randint(1,10)
print("---------kk----------")
a=input("猜猜我现在想的数字是几： ")
b=int(a)
while b!=secret:
    a=input("猜错了重新猜一猜=： ")
    b=int(a)
    if b<secret:
        print("太小了")
    else:
        if b>secret:
            print("太大了")
        else:
            print("你猜对了")
print("yes")
