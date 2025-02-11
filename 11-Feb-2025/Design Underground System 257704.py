# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:
    def __init__(self):
        self.check_ins = {}  
        self.travel_times = {}  
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)
    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_ins:
            startStation, startTime = self.check_ins.pop(id)
            travel_time = t - startTime
            if (startStation, stationName) not in self.travel_times:
                self.travel_times[(startStation, stationName)] = [0, 0]
            self.travel_times[(startStation, stationName)][0] += travel_time
            self.travel_times[(startStation, stationName)][1] += 1
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_times.get((startStation, endStation), (0, 0))
        return total_time / count if count > 0 else 0.0
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)