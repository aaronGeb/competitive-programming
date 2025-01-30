# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:

    def __init__(self):
        self.map ={}
        self.prefix_map = {}
        
    def insert(self, key: str, val: int) -> None:
        prev_val = self.map.get(key,0)
        diff = val - prev_val
        self.map[key] = val
        prefix = ''
        for char in key:
            prefix +=char
            self.prefix_map[prefix] = self.prefix_map.get(prefix,0) + diff
    def sum(self, prefix: str) -> int:
        return self.prefix_map.get(prefix,0)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)