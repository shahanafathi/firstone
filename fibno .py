
def fib(n):
    a =0
    b= 1
    print(a)
    print(b)
    
    for i in range(0, n):
              
            k = a + b
            a = b
            b = k
            print(k)
n = int(input("Enter the range : ")) 
fib(n)

