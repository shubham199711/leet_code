class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            newArr = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
            nums = newArr
        return nums[0]
            
        