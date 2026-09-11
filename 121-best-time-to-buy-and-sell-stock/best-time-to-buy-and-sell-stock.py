class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost = float("inf")
        res = 0
        for i, p in enumerate(prices):
            minCost = min(minCost,p)
            if p == minCost or minCost == float("inf"):
                continue
            if p > minCost:
                res = max(p-minCost, res)
        return res
            
             

