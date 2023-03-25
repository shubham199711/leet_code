class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, item in enumerate(nums):
            diff = target - item
            if cache.get(item) is not None:
                return cache[item], i
            cache[diff] = i
        return -1
