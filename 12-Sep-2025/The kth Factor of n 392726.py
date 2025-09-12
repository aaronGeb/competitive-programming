# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        my_factor = []
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                my_factor.append(i)
                if i!= n//i:
                    my_factor.append(n//i)
        my_factor.sort()
        if k <= len(my_factor):
            return my_factor[k-1]
        return -1
        