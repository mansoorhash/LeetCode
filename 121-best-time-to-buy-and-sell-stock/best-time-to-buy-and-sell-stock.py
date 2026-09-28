class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = float("inf")
        for day_price in prices:
            profit = max(profit, day_price-buy_price)
            buy_price = min(buy_price, day_price)
        return profit



