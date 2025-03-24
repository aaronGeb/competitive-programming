# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        count_zeros = arr.count(0)  
        total_length = n + count_zeros
        i, j = n - 1, total_length - 1

        while i >= 0:
            if j < n:
                arr[j] = arr[i]  
            
            j -= 1

            if arr[i] == 0:  
                if j < n:
                    arr[j] = 0
                j -= 1
            
            i -= 1