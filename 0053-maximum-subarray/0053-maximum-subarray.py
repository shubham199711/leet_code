class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            _max = max(current_sum, _max)
        return _max
