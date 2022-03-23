row=0
while row<=5:
    col=0
    while col<5:
        if row==0 and col%4!=0 or row==3 and col%4!=0 or row!=0 and col==0 or row!=0 and col==4:
            print("*",end=" ")
        else:
            print(" ",end=" ") 
        col=col+1
    row=row+1
    print()
    
    
# n=int(input("enter the number"))
# i=0
# while i<n:
#     k=ord("A")+i
#     j=0
#     while j<=i:
#         print(chr(k),end=" ")
#         k+=1
#         j+=1
#     i+=1
#     print()