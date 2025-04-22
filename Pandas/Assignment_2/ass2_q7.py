str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
unique_chars = set(str1) - set(str2)
print("Letters present in the first string but not in the second:",
      ''.join(unique_chars))
