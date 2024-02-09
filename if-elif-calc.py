a=int(input("enter your number:"))
b=int(input("enter your number:"))
c=input("enter the operation(+,-,/,*) : ")
if c=='+':
    d=a+b
elif c=='-':
    d=a-b
elif c=='*':
    d=a*b
elif c=='/':
    if b!=0:
        d=a/b
    else:
        print(" not divisible")
        exit()
else:
    print(" invalid")
print(f"{a} {c} {b} is {d}")


