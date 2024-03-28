class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for index, item in enumerate(nums):
            if cache.get(item) is not None:
                return cache.get(item), index
            diff = target - item
            cache[diff] = index
        return -1, -1
