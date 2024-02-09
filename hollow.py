
n = 5
k = n - 1

for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1 ):
        
        if j == 0 :
            print("* ", end="")
        elif j==i:
             print("* ", end="")
        elif i==n-1:
            print("* ", end="")
        else:
            print("  ", end="")
    print("")
