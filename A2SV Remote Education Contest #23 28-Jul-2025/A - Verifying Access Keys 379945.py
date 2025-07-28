# Problem: A - Verifying Access Keys - https://codeforces.com/gym/625306/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    dig = []
    letter = []
    is_valid = True

    for ch in s:
        if ch.isdigit():
            if letter: 
                is_valid = False
                break
            dig.append(ch)
        else:
            letter.append(ch)

    if is_valid:
        if dig != sorted(dig) or letter != sorted(letter):
            is_valid = False

    print("YES" if is_valid else "NO")