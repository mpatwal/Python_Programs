def findindex(lis, key):
    for i in range(len(lis)):
        if lis[i] == key:
            return i


lis = eval(input("enter the list : "))
key = (int(input("enter the key : ")))
print(" the index is : ", findindex(lis, key))
