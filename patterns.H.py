# # Like this???????????
# #         1    
# #       1 2  
# #     1 2 3 
# #   1 2 3 4
# # 1 2 3 4 5
# # O/P????????????
n=5
i=1
while i<=5:
    j=1
    while j<=n-i:
        print(" ",end=" ")
        j+=1
    b=1
    while b<=i:  
        print(b,end=" ") 
        b+=1 
    print()
    i=i+1