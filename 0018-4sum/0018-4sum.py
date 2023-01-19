import itertools

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, quad = [], []
        nums.sort()
        def kSum(k, start, currentTarget):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i -1]:
                        continue
                    # quad is buffer where we keep 2 element and then we find remaning with 2-sum solution
                    quad.append(nums[i])
                    kSum(k -1, i + 1, currentTarget - nums[i])
                    quad.pop()
                return
            # base case
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < currentTarget:
                    l += 1
                elif nums[l] + nums[r] > currentTarget:
                    r -= 1
                else:
                    ans.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l -1]:
                        l += 1
        kSum(4, 0, target)
        return ans
