class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_max = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i -1])
            running_max = max(running_max, nums[i])
        return running_max