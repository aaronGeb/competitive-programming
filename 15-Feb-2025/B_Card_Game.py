def distribute_cards(n, cards):
    indexed_cards = [(cards[i], i + 1) for i in range(n)] 
    indexed_cards.sort()  
    
    pairs = []
    for i in range(n // 2):
        pairs.append((indexed_cards[i][1], indexed_cards[n - i - 1][1]))
 
    for pair in pairs:
        print(pair[0], pair[1])
 
# Read input
n = int(input())  
cards = list(map(int, input().split()))  
 

distribute_cards(n, cards)