class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, res = 0, 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i-1])
            res = max(profit, res)
        return res