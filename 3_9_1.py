right = "aaa"
answer = input("请输入密码：")
while True:
    if answer == right:
        break
    answer = input("输入错误，请再次输入：")
print("密码正确")
