## way of the program

## n=int(input("enter the range: "))
## for i in range(n):
##    a=int(input(f"enter the element{i+1}:"))


n = int(input("Enter the range: "))
e = []
for i in range(n):
    a = int(input(f"Enter the element {i + 1}: "))
    e.append(a) 
j=int(input("enter how many max number you want :" ))
x=sorted(e,reverse=True)
c=x[:j]

print(f"largest elements:",c)

