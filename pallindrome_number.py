i=int(input("enter the number:-"))
rev=0
a=i
while i>0:
    rev=rev*10+i%10
    i=i//10
if a==rev:
    print("pallindrome_number")
else:
    print("not pallindrome_number")
