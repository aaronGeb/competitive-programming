# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums[:] =  nums[-k:] + nums[:-k]
        """  
        def reverse(A,x,y):
            while x<y:
                A[x],A[y] = A[y],A[x]
                x +=1
                y -=1
        n = len(nums)
        k = k%n
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)
        """
        