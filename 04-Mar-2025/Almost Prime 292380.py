# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def count_almost_primes(n):
    prime_factors = [0] * (n + 1)  
    # Modified Sieve of Eratosthenes
    for i in range(2, n + 1):
        if prime_factors[i] == 0: 
            for multiple in range(i, n + 1, i):
                prime_factors[multiple] += 1 

    almost_primes = sum(1 for i in range(2, n + 1) if prime_factors[i] == 2)
    
    return almost_primes

# Read input
n = int(input())
print(count_almost_primes(n))