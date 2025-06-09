"""
Write a program to check whether the characters 'd', 'o', and 'g' appear in order in a given string (not necessarily consecutively). 

If they appear in order, print "yes"
Otherwise, print "no"

"""
s = "vcxzxduybfdsobywuefgas"  # try changing this to any string
word = "dog"
index = 0

for char in s:
    if char == word[index]:
        index += 1
    if index == 3:  # found 'd', 'o', 'g' in order
        break

if index == 3:
    print("yes")
else:
    print("no")


# another try

s = "Nabucodonosor"  # try changing this to any string
word = "donor"
index = 0

for char in s:
    if char == word[index]:
        index += 1
    if index == 3:  # found 'd', 'o', 'g' in order
        break

if index == 3:
    print("yes")
else:
    print("no")
