# Problem: Find-the-prefix-common-array-of-two-arrays - https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        count = 0
        seen = set()
        for i in range(len(A)):
            if A[i] in seen:
                count +=1
            if B[i] in seen:
                count +=1
            if A[i] == B[i]:
                count +=1
            seen.add(A[i])
            seen.add(B[i])
            result.append(count)
        return result