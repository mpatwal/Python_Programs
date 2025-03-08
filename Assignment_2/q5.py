n = int(input("Enter an integer: "))

if n <= 1 :
    print("Number should be greater than 1")
else:
    for i in range(2, n + 1):
        if n % i == 0:
            print("Smallest divisor (other than 1):", i)
            break
