class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        _len = len(nums)
        i, r = 0, len(nums) -1
        count = 0
        while i <= r:
            if nums[i] == val:
                del nums[i]
                r -= 1
            else:
                count += 1
                i += 1
        for i in range(_len - len(nums)):
            nums.append(-1)
        return count
        