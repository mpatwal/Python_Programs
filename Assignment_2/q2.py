n=int(input("enter the number : "))
start=int(input("starting : "))
end=int(input("ending : "))
for i in range(start,end+1):
    if i%n==0:
        print(i)
    