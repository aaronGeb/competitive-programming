# Problem: Tram - https://codeforces.com/problemset/problem/116/A

def tram_min_capacity(n: int, stops: list[tuple[int, int]]) -> int:
    current_passengers = 0
    max_capacity = 0

    for exit_count, enter_count in stops:
        current_passengers -= exit_count
        current_passengers += enter_count
        max_capacity = max(max_capacity, current_passengers)

    return max_capacity
if __name__ == "__main__":
    n = int(input())
    stops = [tuple(map(int, input().split())) for _ in range(n)]
    result = tram_min_capacity(n, stops)
    print(result)