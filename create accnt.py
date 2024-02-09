d={}
f={}

def create():
    a=int(input("enter how many accnt if you want: " ))
    for i in range(a):
        k=int(input("enter the accnt number:  "))
        v=int(input("enter the amount: "))
        d[k]=v
        print(" account number {} created with initial amount with {} ".format(k,v))
       
def depst():

        k=int(input("enter the accnt number:  "))
        if k in d:
            v=int(input("enter your amount: "))
            d[k]=v+d[k]
            
            f=d[k]
    
            print(f" the current balance is:{f}") 
            # print(f)
            
          
def disp():
    print(d)
def witdrw():
    k=int(input("enter the accnt number:  "))
    if f>d[k] :
       if k in d:
        v=int(input("enter your amount: "))
        d[k]=d[k]-v
        f[k]=d[k]-f[k]
        print(f" {v} the current balance is:{f}") 
    else:
        print("its insuffcient ")
def delete():
    k=int(input("enter your accnt number :"))
    if k in d:
        del d[k]
        
        print(f" the total amount is:{d}") 
    else:
        print(f"{d}account number is not present:")
while True:
    print("1:create account:\n"
         "2:deposit accnt:\n"
         "3:withdraw accnt:\n"
         "4:delete accnt \n"
         "5:display accnt\n"
         "6:exit\n"
         )
    x=int(input("enter your choice: "))
    if x==6:
        break
    elif x==1:
        create()
    elif x==2:
        depst()
    elif x==3:
        witdrw()
    elif x==4:
        delete()
    elif x==5:
        disp()