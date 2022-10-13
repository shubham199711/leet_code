class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        _ans = [0] * (len(nums) * 2)
        for i, item in enumerate(nums):
            _ans[i] = item
            _ans[i + len(nums)] = item
        return _ans