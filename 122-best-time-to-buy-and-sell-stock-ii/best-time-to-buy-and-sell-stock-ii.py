class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total_profit = 0
        buy_price = prices[0]
        hold_profit = 0
        for day_price in prices:
            day_profit = day_price-buy_price
            if hold_profit > day_profit:
                total_profit += hold_profit
                hold_profit = 0
                buy_price = day_price
            else:
                hold_profit = day_profit
                buy_price = min(buy_price, day_price)
        return total_profit + hold_profit