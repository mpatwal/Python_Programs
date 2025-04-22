dic = {'a': 4, 'w': 2, 't': 1, 'y': 5, 'e': 3, 'c': 5, 'z': 8}
print(dic)
n = input("enter the the key you want to delete : ")
if n in dic:
    del dic[n]
    print("updated dic : ", dic)
else:
    print("key not found")
