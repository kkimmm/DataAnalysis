def save_file(a,b,counts):#封装的文件保存函数
    file_name_A = 'A'+str(count) + '.txt'
    file_name_B = 'B'+str(count) + '.txt'
        
    A_file = open(file_name_A,'w')
    B_file = open(file_name_B,'w')

    A_file.writelines(A)
    B_file.writelines(B)

    A_file.close()
    B_file.close()


f = open('C:\\Users\\MR.G\\Desktop\\test.txt')

A = []
B = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        role,line_s = each_line.split(':',1)
        if role =='A':
            A.append(line_s)
        if role == 'B':
            B.append(line_s)
    
   
        #如果前六个字符不是======说明此处不是对话间的分隔符，
        #即此处进行字符串的分割

    else:
        
        #如果前六个字符是======则判断为对话间的分隔符====......=====

        save_file(A,B,count)
       

        A = []
        B = []
        
        count += 1


save_file(A,B,count)

f.close()

