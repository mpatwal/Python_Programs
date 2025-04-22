info = {
    1001: [1, 'riya', 40],
    1002: [2, 'tiya', 34],
    1003: [3, 'siya', 39],
    1004: [4, 'miya', 46],
    1005: [5, 'diya', 36]
}
n = int(input("admission number : "))
if n in info:
    print("student information : ")
    for val in info[n]:
        print(val)
else:
    print("no information ")
