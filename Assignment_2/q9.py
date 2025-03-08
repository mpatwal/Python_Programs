import math
def compute_euler(n_terms):
    e = 1  
    fact = 1 
    for i in range(1, n_terms):
        fact *= i  
        e += 1 / fact 
    return e
n = int(input("Enter the number of terms: "))
print(int(compute_euler(n)))
