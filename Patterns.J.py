# Like this ???????
#           1    
#         2 1  
#      3  2 1 
#    4 3  2 1 
# 5 4 3  2  1

i=0
while i<6:
    print('  '*(5-i),end=" ")
    j=0
    while j-1<i*2:
        if j+1>i+1:
            print((i*2)-j+1,end=" ")
        j+=1
    print()
    i+=1
    
     