# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.schedule = SortedDict()
        

    def book(self, startTime: int, endTime: int) -> bool:
        i = self.schedule.bisect_right(startTime)
        if i < len(self.schedule) and self.schedule.values()[i] < endTime:
            return False
        self.schedule[endTime] = startTime
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)