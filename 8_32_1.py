file_name = input('请输入需打印的文件名称（需要输入路径）：')
f = open(file_name)
print('文件内容是')
for each_line in f:
    print(each_line)
