first=0
second=1
a=int(input("Enter number up to factorial"))
print(first)
print(second)
for i in range(first,a):
    next=first+second
    first=second
    second=next
    print(next)