try:
    sum = 1 + '1'
    f = open('hh.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('没有对应的文件\n错误的原因是：'+str(reason))
except TypeError as reason:
    print('类型出错了\n错误的原因是：'+str(reason))
