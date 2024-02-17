import itertools

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, demp = [], []
        nums.sort()
        def k_sum(k, start, current_target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    demp.append(nums[i])
                    k_sum(k - 1, i + 1, current_target - nums[i])
                    demp.pop()
                return 
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < current_target:
                    l += 1
                elif nums[l] + nums[r] > current_target:
                    r -= 1
                else:
                    ans.append(demp + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        k_sum(4, 0, target)
        return ans