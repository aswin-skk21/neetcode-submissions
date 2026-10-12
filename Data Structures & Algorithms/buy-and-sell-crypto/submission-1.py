class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]
        for price in prices:
            profit = max(profit, price - min)
            if price < min: 
                min = price 

        return profit