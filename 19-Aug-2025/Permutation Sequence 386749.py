# Problem: Permutation Sequence - https://leetcode.com/problems/permutation-sequence/description/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        numbers = list(range(1, n + 1))
        k -= 1  
        result = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            result.append(str(numbers.pop(index)))
            k %= fact

        return ''.join(result)