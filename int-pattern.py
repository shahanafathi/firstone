# for i in range(65,70):
#     for j in range(65,i+1):
#        print(chr(j),end=' ')
# #     print() 
# n= int (input("enter your number"))
# for i in range(1,n):
#     for j in range(1,i+1):
#        print(int(j),end=' ')
#     print() 

for i in range(0, 5):
    for j in range(0, 5-i):
        print(" ", end=" ")
val = 1
for j in range(0, i+1):
 print(val, end=" ")
val = val * (i - j) // (j + 1)
print()