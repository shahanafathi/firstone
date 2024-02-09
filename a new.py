# row = int (input ("Please enter how many rows you need: "))  
# for i in range (row+1):  
#     for j in range (i):  
#         print(i,end = " ")  
#     print () 

rows = int(input("Please enter how many rows you need: "))  
for i in range(1, rows+1):  
    for j in range(1, i + 1):  
        print(j, end=' ')  
    print('')  