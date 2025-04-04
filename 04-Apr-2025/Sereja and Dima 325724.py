# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
cards = list(map(int, input().split()))

left, right = 0, n - 1
sereja_score, dima_score = 0, 0
turn = 0 

while left <= right:
    if cards[left] > cards[right]:
        chosen_card = cards[left]
        left += 1
    else:
        chosen_card = cards[right]
        right -= 1

    if turn % 2 == 0:
        sereja_score += chosen_card
    else:
        dima_score += chosen_card

    turn += 1

print(sereja_score, dima_score)