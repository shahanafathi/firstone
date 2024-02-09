n = int(input("Enter the range: "))
c = []
for i in range(n):
   a = int(input(f"Enter the element {i + 1}: "))
   c.append(a)
while True:   
   j=int(input("enter how many max number you want :" ))
   if j>n:
      break
   else:
      x=sorted(c,reverse=True)
      b=x[:j]
      print(f"Largest element: {b}")

