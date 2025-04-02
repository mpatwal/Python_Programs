li = input("enter the string : ")
w = input("enter the character you want to search : ")


def counting(w, li):
    ch = 0
    for i in li:
        if i == w:
            ch += 1
    return ch


print(counting(w, li))
