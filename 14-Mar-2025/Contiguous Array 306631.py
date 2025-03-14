# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_leng = 0
        one = zero = 0
        indx_map =  {}

        for i,n in enumerate(nums):
            if n == 0:
                zero +=1
            else:
                one +=1
            if zero - one not in indx_map:
                indx_map[zero -  one] = i
            if one == zero:
                max_leng = one + zero
            else:
                idx = indx_map[zero - one]
                max_leng = max(max_leng, i -  idx)
        return max_leng

        