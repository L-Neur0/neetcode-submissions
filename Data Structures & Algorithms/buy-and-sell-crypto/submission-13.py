class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        l, r = 0, 0 

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])

        return max_profit