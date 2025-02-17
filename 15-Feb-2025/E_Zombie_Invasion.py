def can_survive(n, k, a, x):
    # Pair each zombie's health with its distance
    zombies = sorted(zip(a, map(abs, x)), key=lambda z: z[1])
    
    total_bullets = 0
    for health, distance in zombies:
        total_bullets += health
        if total_bullets > k * distance:
            return False
    return True

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n, k = int(data[idx]), int(data[idx + 1])
        idx += 2
        a = list(map(int, data[idx:idx + n]))
        idx += n
        x = list(map(int, data[idx:idx + n]))
        idx += n
        if can_survive(n, k, a, x):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()