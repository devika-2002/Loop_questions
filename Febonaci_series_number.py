n=int(input("enter the number"))
i=0
b=1
c=0
while i<n:
    # print(c)
    i=b
    b=c
    c=i+b
    print("Febonaci_number:-",c)

