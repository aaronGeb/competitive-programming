# Problem: B - Hit the Lottery - https://codeforces.com/gym/637748/problem/B

n = int(input())
bills = [100, 20, 10, 5, 1]
count = 0
for bill in bills:
    count += n // bill
    n %= bill
print(count)