class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        _len = len(nums)
        for i in range(_len):
            item = nums[i]
            item = int(str(item)[::-1])
            nums.append(item)
        return len(set(nums))