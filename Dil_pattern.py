                    # For_loop
n=7
for i in range(n):
    for j in range(n):
        if (j==0 or j==6)and(i==1 or i==2)or(j==1 or j==5)and(i==0 or i==3)or(j==2 or j==4)and(i==0 or i==4)or(j==3 and(i==1 or i==5)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


                            #While_Loop
i=0
while(i<n):
    j=0
    while(j<n):
        if (j==0 or j==6)and(i==1 or i==2)or(j==1 or j==5)and(i==0 or i==3)or(j==2 or j==4)and(i==0 or i==4)or(j==3 and(i==1 or i==5)):
           print("*",end=" ")
        else:
            print(" ",end=" ") 
        j+=1
    print()
    i+=1