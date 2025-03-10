# Problem: C - Robin’s Water Wisdom: Stop the Leaks! - https://codeforces.com/gym/594356/problem/C

def stop_leaks(n, A, B, sizes):
    s1 = sizes[0]
    max_sum = (s1 * A) / B
    ts = sum(sizes)
    if ts <= max_sum:
        print(0)
        return 
    sizes[1:] = sorted(sizes[1:], reverse=True)
    b = 0
    for size in sizes[1:]:
        ts -= size
        b += 1
        if ts <= max_sum:
            print(b)
            return

if __name__ == "__main__":
    n, A, B = map(int, input().split())
    sizes = list(map(int, input().split()))
    stop_leaks(n, A, B, sizes)