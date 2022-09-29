class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, item in enumerate(nums):
            if table.get(item) is not None:
                return [table.get(item), i]
            _sub = target - item
            table[_sub] = i
        return []
