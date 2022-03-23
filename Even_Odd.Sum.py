n=int(input("enter the number"))
i=0
odd=0
even=0
while i<=n:
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
    i=i+1
print("total sum of odd is :",odd)
print("total sum of even is :",even)
