d={}
def  create():
    a=int(input("enter how many pairs: "))
    for i in range(a):
        k=(input("enter your name: "))
        v=int(input("enter your contact: "))
        d[k]=v
    print("creted")
def disp():
     print(d)
def update():
    
        k=(input("enter your name: "))
        if k in d:
          v=int(input("enter your contact: "))
          d[k]=v 
          print("update")
        else:
          print(f"{k} not in list") 
def delete():
    
        k=(input("enter your name: "))
        if k in d:
          
          del d[k]
          print("delete")
        else:
          print(f"{d} not in list") 

while True:
    print("1:create:\n"
         "2:updte:\n"
         "3:delete:\n"
         "4:display\n"
         "5:exit\n"
         )
    x=int(input("enter your choice: "))
    if x==5:
        break
    elif x==1:
        create()
    elif x==2:
        update()
    elif x==3:
        delete()
    elif x==4:
        disp()
  


    
 