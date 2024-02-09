# up
# n = 5
# k = n - 1
# for i in range(0, n):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")

 #down
# n = 5
# k = n - 1
# for i in range(n,0, -1):
#     for j in range(k):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i ):
#         print("* ", end="")
#     print("")
 
    #full

# n = 5
# k = n - 1
# for i in range(0, n):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i + 1):

#         print("* ", end="")
#     print("")
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(end=" ")
#     for j in range(0, i-1):
#         print(" *", end="")
#     print("")
    

#hollow

n = 5
k = n - 1

for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        
        if j == 0 :
            print("* ", end="")
        elif j==i:
             print("* ", end="")
        else:
            print("  ", end="")
    print("")

for i in range(n, 0, -1):
    for j in range(n - i):
        print(end=" ")
    for j in range(0, i-1):
        if j == 0 :
            print(" *", end="")
        elif j ==n-1:
            print(" * ", end="")
        else:
            print("  ", end="")    
    print("")