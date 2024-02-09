# i=int(input("enter the num ber :"))

# if i<=100:
#       if i*15:
#        print("for the first 100 liter:")
#       elif i*14:
#        print("for the next 100 liter:")
# else:
#     t=100*15+100*14+(i-200)*12
# print("total water bill:Rs.",i,t)
# if i==100:
#   if i*15:
#      print("for the first liter:")
# if i==i+100:
#     if i*14:
#      print("for the secound  liter:")
# if i==200:
#     if i*12:
#      print("for the third liter:")
# else :
#     print("")

#correct code

# i=int(input("enter the number:"))

# if i<0 and i<=100:
#   a=i*15
# if i>101 and i<=200:
  
#   a=100*15+14*(i-100)
# if i>=201:
#   a=100*15+100*14+12*(i-200)
# print("the total is:",a)
   
  
# def wtr(i):
  
#   if i<0 and i<=100:
#     return  i*15 
   
#   elif i>101 and i<=200:
#     return  100*15+14*(i-100)
  
#   elif i>=201:
#      return  100*15+100*14+12*(i-200)
#   b=wtr(i)
#   print(b)
# i=int(input("enter the number:"))


def wtr():
  i=int(input("enter the number:"))
  
  if i<0 and i<=100:
    print(i*15) 
   
  elif i>101 and i<=200:
   print(100*15+14*(i-100))
  
  elif i>=201:
    print(100*15+100*14+12*(i-200))


wtr()
