# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())
chat_order = []
chat_positions = {}

for _ in range(n):
    friend = input().strip()
    if friend in chat_positions:
        chat_order.pop(chat_positions[friend])
    chat_order.insert(0, friend)
    for i, name in enumerate(chat_order):
        chat_positions[name] = i

# Print the final chat order
for name in chat_order:
    print(name)