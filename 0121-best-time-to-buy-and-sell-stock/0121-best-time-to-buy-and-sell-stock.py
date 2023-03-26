class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        runnigMin = prices[0]
        runningMaxDiff = 0
        for item in prices:
            runnigMin = min(runnigMin, item)
            runningMaxDiff = max(runningMaxDiff, item - runnigMin)
        return runningMaxDiff
        