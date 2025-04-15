# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

def can_kirito_win(s, dragons):
    dragons.sort()
    
    for dragon_strength, bonus in dragons:
        if s > dragon_strength:
            s += bonus
        else:
            return "NO"
    return "YES"

# Input handling
s, n = map(int, input().split())
dragons = [tuple(map(int, input().split())) for _ in range(n)]

print(can_kirito_win(s, dragons))