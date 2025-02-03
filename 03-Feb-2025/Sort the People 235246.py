# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = dict(zip(heights,names))
        return [people[h] for h in sorted(people.keys(), reverse=True)]

        