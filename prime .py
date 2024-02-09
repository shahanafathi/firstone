def prime(n):
    if n>1:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                print("not prime")
                break
        else: 
            print("its a prime")
    else:
        print("its not a prime")        
n=int(input("enter the number: "))
prime(n)