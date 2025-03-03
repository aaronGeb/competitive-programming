# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for value_to_sort in range(len(arr), 1, -1):
            max_index = arr.index(value_to_sort)
            if max_index != value_to_sort - 1:
                if max_index != 0:
                    result.append(max_index + 1)
                    arr[:max_index + 1] = reversed(arr[:max_index + 1])
                result.append(value_to_sort)
                arr[:value_to_sort] = reversed(arr[:value_to_sort])
        
        return result
