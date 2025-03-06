# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_max = -1
        n = len(arr)
        for i in range(n-1,-1,-1):
            current_elm = arr[i]
            arr[i] = max_max
            max_max = max(max_max, current_elm)
        return arr

        