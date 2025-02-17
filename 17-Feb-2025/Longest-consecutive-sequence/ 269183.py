# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_num = set(nums)
        longest_length = 0
        for num in my_num:
            if num - 1 not in my_num:
                current_num = num
                current_leng = 1
                while current_num +1 in my_num:
                    current_num +=1
                    current_leng +=1
                longest_length = max(longest_length,current_leng)
        return longest_length
        