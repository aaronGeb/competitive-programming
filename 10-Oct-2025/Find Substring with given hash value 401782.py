# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        res_index = 0
        current_hash = 0
        power_k = pow(power, k, modulo)  
        for i in range(n - 1, -1, -1):
            val = ord(s[i]) - ord('a') + 1
            current_hash = (current_hash * power + val) % modulo
            if i + k < n:
                remove_val = ord(s[i + k]) - ord('a') + 1
                current_hash = (current_hash - remove_val * power_k) % modulo
            if current_hash == hashValue:
                res_index = i

        return s[res_index:res_index + k]