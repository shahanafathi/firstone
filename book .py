a=[]
b=[]


# print(b)
while True:
     print("1:Add Book\n"
         "2:Display book\n"
         )
     x=int(input("enter your choice:"))
     if x==3:
        break
     elif x==1:
         
         book_id=int(input("enter your book-id:"))
         name=input("enter your name :")
         price=int(input("enter your price:"))
         auther=input("enter your auther:")
         publisher=input("enter your publisher:")
         
         b.append(book_id)
         b.append(name)
         b.append(price)
         b.append(auther)
         b.append(publisher)
         a.append(b)
        
     elif x==2:

         print(a)
    
    
    
   