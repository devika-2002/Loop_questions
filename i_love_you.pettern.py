for i in range(7):
    for j in range(10):
        print(" ",end=" ")
    for j in range(5):
        if ((i==0 or i==6)and(j>=0 and j<=4))or(j==2 and(i>0 and i<6)):
            print("*",end=" ")
        else: 
            print(" ",end=" ")
    print()

n=7
for i in range(n):
    for j in range(9):
        print(" ",end=" ")
    for j in range(n):
        if (j==0 or j==6)and(i==1 or i==2)or(j==1 or j==5)and(i==0 or i==3)or(j==2 or j==4)and(i==0 or i==4)or(j==3 and(i==1 or i==5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(7):
    for j in range(10):
        print(" ",end=" ")
    for j in range(6):
        if (j==0 or j==5)and(i>=0 and i<5)or(i==5)and(j>0 and j<5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()