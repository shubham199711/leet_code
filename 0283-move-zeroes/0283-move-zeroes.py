class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0
        while l < len(nums):
            if nums[l] == 0:
                while True:
                    if r >= len(nums):
                        return
                    if nums[r] != 0:
                        nums[l], nums[r] = nums[r], nums[l]
                        r += 1
                        break
                    r += 1
                l += 1
            else:
                l += 1
                r = l