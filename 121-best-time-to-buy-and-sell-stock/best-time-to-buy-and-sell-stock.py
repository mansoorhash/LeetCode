class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = float("inf")
        for i, day_price in enumerate(prices):
            if buy_price != float("inf"):
                profit = max(profit, day_price-buy_price)
            if day_price < buy_price:
                buy_price = day_price
        return profit



