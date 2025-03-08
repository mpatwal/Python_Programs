n=int(input("enter the number : "))
sum=0
while n>0:
    sum=int(sum+(n%10))
    n=n/10
print("sum of digits is : ",sum)