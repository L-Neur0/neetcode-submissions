class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        profit = 0
        profit_max = 0
        for n in range(1, len(prices)):
            if prices[n] > cur_min:
                profit = prices[n] - cur_min
                profit_max = max(profit_max, profit)
                print(profit_max)
            else:
                cur_min = prices[n]
        return profit_max