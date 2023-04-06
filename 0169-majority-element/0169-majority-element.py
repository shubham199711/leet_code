class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cache = {}
        _max = 0
        char = ''
        for item in nums:
            if cache.get(item) is not None:
                cache[item] += 1
            else:
                cache[item] = 1
            if _max < cache[item]:
                _max = cache[item]
                char = item
        return char
        