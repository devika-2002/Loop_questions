# 1 2 3 4 5
# 2 2 3 4 5 
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

s=5
i=1
while i<=5:
    j=1
    while j<=5:
        if j<i:
            print(i,end=" ")
        else:
            print(j,end=" ")
        j=j+1
    print()
    s=s+1
    i=i+1