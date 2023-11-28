class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if(prices[i] < prices[i - 1]):
                profit += (prices[i - 1] - buy)
                buy = prices[i]
        profit += (prices[-1] - buy)
        return profit
        