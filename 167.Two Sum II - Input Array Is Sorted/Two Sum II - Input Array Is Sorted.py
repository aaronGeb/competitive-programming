class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       lPoint, rPoint = 0,len(numbers)-1
       while lPoint < rPoint:
            tsum = numbers[lPoint] + numbers[rPoint]
            if tsum == target:
                return [lPoint+1,rPoint+1]
            elif tsum < target:
                lPoint +=1
            else:
                rPoint -=1