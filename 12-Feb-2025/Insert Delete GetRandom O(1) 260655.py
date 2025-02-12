# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.nums = []  
        self.indices = {} 

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
      
        last_element = self.nums[-1]
        idx = self.indices[val]
        
        self.nums[idx] = last_element  
        self.indices[last_element] = idx 
        
     
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()