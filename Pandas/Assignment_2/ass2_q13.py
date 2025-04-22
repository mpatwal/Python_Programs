str = input("enter the string : ")
with open("output.txt", "a") as file:
    file.write(str + "\n")
print(" string appended successfully")
with open("output.txt", "r") as file:
    print("current contents of the file : ")
    print(file.read())
