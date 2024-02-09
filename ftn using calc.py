def calcu(a,b):
    return a+b
def calcu1(a,b):
    return a-b
def calcu2(a,b):
    return a*b
def calcu3(a,b):
    return a/b


while True:
    print("1:additional\n"
         "2:sub\n"
         "3:mult\n"
         "4:div\n"
         )
   
    x=int(input("enter your choice:"))
    if x==5:
        break
    elif x==1:
     a=int(input("enter your number"))
     b=int(input("enter your number"))
     sum=calcu(a,b)
     print(sum)
    elif x==2:
     a=int(input("enter your number"))
     b=int(input("enter your number"))
     sub=calcu1(a,b)
     print(sub)
    elif x==3:
     a=int(input("enter your number"))
     b=int(input("enter your number"))
     mul=calcu2(a,b)
     print(mul)
    elif x==4:
     a=int(input("enter your number"))
     b=int(input("enter your number"))
     div=calcu3(a,b)
     print(div)