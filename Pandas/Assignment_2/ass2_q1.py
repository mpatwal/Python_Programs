num = [12, 4, 34, 23, 5, 14, 90]
large = num[0]
sl = -1
for i in range(1, len(num)):
    if num[i] > large:
        sl = large
        large = num[i]

    elif num[i] > sl and num[i] != large:
        sl = num[i]
print(sl)
