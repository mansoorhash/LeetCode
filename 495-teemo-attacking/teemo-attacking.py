class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0: return 0
        total = 0
        for i in range(len(timeSeries)):
            next_val = 0
            if i + 1 < len(timeSeries):
                next_val = timeSeries[i+1]
            eff = timeSeries[i] + duration
            if next_val and eff > next_val:
                total += next_val - timeSeries[i]
            else:
                total += duration
        
        return total
            


