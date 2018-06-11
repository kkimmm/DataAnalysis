s=int(input("请输入一个分数："))
if 90 <= s <= 100:
    print("A")
elif 80 <= s < 90:
    print("B")
elif 70 <= s < 80:
    print("C")
elif 60 <= s < 70:
    print("D")
elif  s < 60:
    print("E")
elif  s > 100:
    print("输入的数字不能大于100")
