#square

# n = 5

# for i in range(0, n):
#     for j in range(0, n):
#         print("*", end=" ")
#     print()
    
    #hollow sqr

n = 5

for i in range(n):
    for j in range(n):
      if i==0:
        print("*", end=" ")
      elif i==n-1:
        print("*", end=" ")
      elif j==0:
        print("*", end=" ")
      elif j==n-1:
        print("   *", end=" ")
      else:
        print(" ",end="")
    print()
    


