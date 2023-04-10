class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        _sum = 0
        seenBeforeDict = { 0 : 1} # if we count (sum - k) == 0 then ans should be increment by 1
        for item in nums:
            _sum += item
            if _sum - k in seenBeforeDict:
                ans += seenBeforeDict[_sum - k]
            seenBeforeDict[_sum] = seenBeforeDict.get(_sum, 0) + 1 # store current sum as key and value as (prev as key or 0) + 1
        return ans
        