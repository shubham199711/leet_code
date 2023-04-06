class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set([])
        for i, item in enumerate(nums):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                _sum = item + nums[lo] + nums[hi]
                if _sum == 0:
                    ans.add((item, nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                elif _sum < 0:
                    lo += 1
                else:
                    hi -= 1
        return ans
