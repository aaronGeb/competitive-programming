# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for i in range(1, n+1):
            total ^= i
        odd_xor = 0
        for i in range(1, len(encoded), 2):
            odd_xor ^= encoded[i]

        perm = [0] * n
        perm[0] = total ^ odd_xor
        for i in range(len(encoded)):
            perm[i+1] = perm[i] ^ encoded[i]

        return perm
