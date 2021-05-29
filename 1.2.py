A=[]; B=[]; C=[]
import random
n=int(input('Nhập số phần tử List A: ' ))
m=int(input('Nhập số phần tử List B: ' ))
while n<=0 or m<=0:
        n=int(input('n phải là số nguyên dương. Hay Nhập lại: '))
        m=int(input('m phải là số nguyên dương. Hay Nhập lại: '))
for i in range(1,n+1):
    giatri=random.randint(-100,100) 
    A.append(giatri)
for j in range(1,m+1):
    giatri=random.randint(-100,100)
    B.append(giatri)
print ('A = ',A)
print ('B = ',B)
C.extend(A)
C.extend(B)
print('C=',C)
C.sort()
print('C=',C)
x=int(input('Nhập số nguyên x: ' ))
if x in C:
    i=C.index(x)
    print (x,' xuất hiện đầu tiên tại vi tri: C[',i,'], Giá trị: ',C[i])
else:
    print (x,' không xuất hiện trong C')
C2 = []
for i in C:
    if i not in C2:
        C2.append(i)
print('C mới=',C2)
