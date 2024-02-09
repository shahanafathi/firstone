#ptrn 1
n = 5
for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print()


#pattern 2
n = 5
for i in range(0, n):
    for j in range(0, i + 1):
        print("* ", end="")
    print()
for i in range(n, 0, -1):
    for j in range(0, i-1):
        print("* ", end="")
    print()


# pattern 3:
n = 5

for i in range(0, n):
    for j in range(0,-1,n):
        print(" ", end=" ")
    for j in range(0,2*i-1):
        print(" * ", end=" ")

    print()


# pattern 4

n=5
for i in range(0,n):
    for j in range(0, i+1):
        print("* ",end="")
    print()
    
#pattern5

n=5
for i in range(0,n):
    for j in range(0,n-i):
        print(" * ",end="")
    print()
    
 #   pattern 6 (reference)
 
n = 5
for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end=" ")
    for j in range(0, 2*i+1):
        print("*", end=" ")
    print()

#pattern 6-using k=k-1-down-triangle

n=5
k=n-1
for i in range (0,n):
    for j in range (0,k):
        print(end=" ")
    k=k+1
    for j in range(1,n-i+1):
        print("* ",end="")
    print("")   
    
    