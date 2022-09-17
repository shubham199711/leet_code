class Solution:
    def helper(self, nums, index, _sum, target, memo = {}):
        if index == len(nums):
            if target == _sum:
                return 1
            return 0
        i = f'{index},{_sum}'
        if memo.get(i) is not None:
            return memo[i]
        positive = self.helper(nums, index + 1,_sum + nums[index], target, memo)
        negetive = self.helper(nums, index + 1,_sum - nums[index], target, memo)
        _localSum = positive + negetive
        memo[i] = _localSum
        return _localSum
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, 0, target, {})
        
        