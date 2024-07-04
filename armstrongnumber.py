number=int(input("Enter the number"))
sum=0
order=len(str(number))
a=number
while(number>0):
    digit=number%10
    sum=sum+digit**order
    number=number//10
if(sum==a):
    print("Armstrong number")
else:
    print("Not an armstrong number")