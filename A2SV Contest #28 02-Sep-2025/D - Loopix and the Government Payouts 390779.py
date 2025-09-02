# Problem: D - Loopix and the Government Payouts - https://codeforces.com/gym/632067/problem/D

def solve():
    n = int(input())
    initial_wealth = list(map(int, input().split()))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
        
    final_wealth = [0] * n
    is_finalized = [False] * n
    max_payout_floor = 0
    for query in reversed(queries):
        event_type = query[0]
        
        if event_type == 1:
            p, x = query[1] - 1, query[2] 
            if not is_finalized[p]:
                final_wealth[p] = max(x, max_payout_floor)
                is_finalized[p] = True
        else: 
            x = query[1]
            max_payout_floor = max(max_payout_floor, x)
    for i in range(n):
        if not is_finalized[i]:
            final_wealth[i] = max(initial_wealth[i], max_payout_floor)
            
    print(*final_wealth)

solve()