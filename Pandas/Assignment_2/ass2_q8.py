str1 = input("Enter the string : ")
str2 = ""
i = 0
for ch in str1:
    if i % 2 == 0:
        str2 += ch
        i += 1
    else:
        ch = ch.upper()
        str2 += ch
        i += 1
print("String before change: " + str1)
print("String after change: " + str2)
