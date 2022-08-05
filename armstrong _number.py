n=int(input("enter the number:-"))
sum=0
b=n
while b>0:
    digit=b%10
    sum+=digit**3
    b//=10
if n==sum:
    print("this is armstrong number:-")
else:
    print("this is armstrong number:-")