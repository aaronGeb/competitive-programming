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




******************correct option*****************
def chat_order(messages):
    seen = set() 
    output = []  

    for message in reversed(messages):
        if message not in seen:
            seen.add(message)
            output.append(message)

    return "\n".join(output) 

t = int(input())
message = []
for _ in range(t):
    message.append(input())

print(chat_order(message))
