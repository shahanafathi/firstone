#full

n = 5
for i in range(0, n):
    for j in range(0, i+1):
        print("* ", end="")
    print()
# for i in range(n, 0, -1):
    for j in range(0, i-1):
        print("* ", end="")
    print()

# fst part 

# n = 5
# for i in range(0, n):
#     for j in range(0, i+1):
#         print("* ", end="")
#     print()

#2nd part
# n = 5
# for i in range(0, n):
#     for j in range(0, n-i):
#         print("* ", end="")
#     print()