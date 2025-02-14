# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:

    def __init__(self):
        self.num_count ={}
        self.freq_count = {}
        

    def add(self, number: int) -> None:
        if number in self.num_count:
            old_freq = self.num_count[number]
            self.freq_count[old_freq] -=1
            if self.freq_count[old_freq] == 0:
                del self.freq_count[old_freq]
            self.num_count[number] +=1
        else:
            self.num_count[number] = 1
        new_freq = self.num_count[number]
        self.freq_count[new_freq] = self.freq_count.get(new_freq, 0) + 1
        

    def deleteOne(self, number: int) -> None:
        if number in self.num_count:
            old_freq = self.num_count[number]
            self.freq_count[old_freq] -= 1
            if self.freq_count[old_freq] == 0:
                del self.freq_count[old_freq]

            if old_freq > 1:
                self.num_count[number] -= 1
                new_freq = self.num_count[number]
                self.freq_count[new_freq] = self.freq_count.get(new_freq, 0) + 1
            else:
                del self.num_count[number]
        

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_count
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)