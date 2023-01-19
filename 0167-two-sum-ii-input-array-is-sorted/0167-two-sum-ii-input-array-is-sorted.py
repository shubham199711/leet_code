class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            _sum = nums[l] + nums[r]
            if _sum < target:
                l += 1
            elif _sum > target:
                r -= 1
            else:
                return l + 1, r + 1