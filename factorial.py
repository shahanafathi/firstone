#1st try
 
# n=int(input("enter the number:"))
# for i in range(1,n):
#     n=n*i
#     print(n)

# #2nd try

# n=int(input("enter the number:"))
# a=1
# for i in range(1,n+1):
#     a=a*i
#     print(a)

#  3rdtry  -using ftn

# def fact(n):
#     n=1
#     for i in range(1,n+1):
#         r=n*i
#         return r
#     a=fact(n)
#     print(a)
# n=int(input("enter the number:"))

#4th try
# def fact(n):
#     for i in range(1, n + 1):
#         k = n * i
#     return k
       
# n = int(input("Enter the number:"))
# a = fact(n)
# print(a)

#5th try

# def fact(n):

#     for i in range(1, n):
#          n= n * i
#     return n
# c=int(input("Enter the range to:"))  
# # n=int(input("enter the number:"))
# for x in range(1,c+1):
#   a = fact(x)
#   print(a)

 #6th try

# def fact(n):
#     b = 1
#     for i in range(1, n + 1):
#         b *= i
#     return b

# c = int(input("Enter the range to:"))

# for x in range(1, c + 1):
#     a = fact(x)
#     print(a)




def fact(n):
    b = 1
    
    for i in range(1, n + 1):
        b *= i
    return b
n = int(input("Enter the range to:"))
a = fact(n)
print(a)
