# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

def process_array(arr):
    has_odd = any(x % 2 == 1 for x in arr)
    has_even = any(x % 2 == 0 for x in arr)

    if has_odd and has_even:
        arr.sort()
    
    print(*arr)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    process_array(arr)
