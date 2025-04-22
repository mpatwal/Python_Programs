import ast


def nested_sum(lis):
    total = 0
    for item in lis:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total


numlist = ast.literal_eval(input("Enter the list: "))
totalsum = nested_sum(numlist)
print("Total sum of nested list:", totalsum)
