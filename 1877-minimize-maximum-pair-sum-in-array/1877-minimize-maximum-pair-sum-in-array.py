class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        _max = float('-inf')
        for i in range(len(nums)):
            _max = max(_max, nums[i] + nums[-i-1])
        return _max
            