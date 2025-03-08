def sieve_of_eratosthenes(start, end):
    if end < 2:
        print("No prime numbers in this range.")
        return
    primes = [True] * (end + 1)  
    primes[0] = primes[1] = False  
    for num in range(2, int(end ** 0.5) + 1):
        if primes[num]:  
            for multiple in range(num * num, end + 1, num):
                primes[multiple] = False 
    for num in range(max(2, start), end + 1):
        if primes[num]:
            print(num, end=" ")

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end}:")
sieve_of_eratosthenes(start, end)
