# Problem: Day at the Beach - https://codeforces.com/problemset/problem/599/C

def max_blocks(n, heights):
    prefix_max = [0] * n
    suffix_min = [0] * n

    prefix_max[0] = heights[0]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i - 1], heights[i])

    suffix_min[-1] = heights[-1]
    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(suffix_min[i + 1], heights[i])

    count = 0
    for i in range(n - 1):
        if prefix_max[i] <= suffix_min[i + 1]:
            count += 1

    return count + 1

if __name__ == "__main__":
    n = int(input())
    heights = list(map(int, input().split()))
    result = max_blocks(n, heights)
    print(result)
