# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total_rabbits = 0
        for r,freq in count.items():
            group_size =r +1
            num_groups = math.ceil(freq/group_size)
            total_rabbits += num_groups * group_size
        return total_rabbits

        