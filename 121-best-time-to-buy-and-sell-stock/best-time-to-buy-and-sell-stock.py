class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        low = float('inf')
        for p in prices:
            low = min(low,p)
            s = max(s, p - low)
            print()
        return s

