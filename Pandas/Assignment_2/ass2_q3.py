def odd_time(num):
    return (n for n in num if num.count(n) % 2 != 0)


num = [2, 3, 3, 1, 6, 6, 5, 5, 8, 9, 9]
print(list(odd_time(num)))
