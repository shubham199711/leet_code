class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        _ans = {}
        nums.sort()
        for i, item in enumerate(nums):
            li, hi = i + 1, len(nums) - 1
            while li < hi:
                _sum = item + nums[li] + nums[hi]
                if _sum == 0:
                    key = (item, nums[li], nums[hi])
                    _ans[key] = True
                    li += 1
                    hi -= 1
                elif _sum < 0:
                    li += 1
                else:
                    hi -= 1
        return list(_ans.keys())