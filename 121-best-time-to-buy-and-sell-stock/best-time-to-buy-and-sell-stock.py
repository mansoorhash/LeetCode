class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s = 0
        low = prices[0]
        for p in prices:
            low = min(low,p)
            s = max(s, p - low)
        return s

