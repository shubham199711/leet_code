class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, x in enumerate(nums):
            y = target - x
            if cache.get(x) is not None:
                return cache[x], i
            cache[y] = i
        return [-1, -1]
