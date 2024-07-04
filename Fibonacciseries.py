f=1
a=int(input("Enter a number"))
if a<0:
    print("factorial cannot be find")
elif a==0:
    print("factorial of a is 1")
else :
    for i in range(1,a+1):
        f=f*i
    print("factorial of a is: ",f)