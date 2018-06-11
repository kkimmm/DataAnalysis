f = open('C:\\Users\\MR.G\\Desktop\\test.txt')
A = []
B = []
count = 1

for each_line in f:
    role,line_s = each_line.split(':',1)
    if role == 'A':
        A.append(line_s)
    if role == 'B':
        B.append(line_s)
        
    A_file = open('C:\\Users\\MR.G\\Desktop\\A_1.txt','w')
    B_file = open('C:\\Users\\MR.G\\Desktop\\B_1.txt','w')

    A_file.writelines(A)
    B_file.writelines(B)

    A_file.close()
    B_file.close()

  

    
f.close()
