class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        _ans = []
        for item in nums:
            _ans.append(nums[item])
        return _ans
        