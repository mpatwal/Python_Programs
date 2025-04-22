def count(str):
    words = str.lower().split()
    w_f = {}

    for word in words:
        if word in w_f:
            w_f[word] += 1
        else:
            w_f[word] = 1

    return w_f


str = input("enter the string : ")
w_f = count(str)
print(w_f)
