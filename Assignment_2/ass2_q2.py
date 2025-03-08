def odd_neg(numb):
    return [n for n in numb if n >= 0 and n % 2 == 0]


numb = [-2, 34, 12, 4, 3, 5, -4, -5]
new_numb = odd_neg(numb)
print("New list : ", new_numb)
