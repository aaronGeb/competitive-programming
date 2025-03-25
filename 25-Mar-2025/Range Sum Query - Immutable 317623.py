# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = list(accumulate(nums))
        self.prefix_sum.append(0)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - self.prefix_sum[left -1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)