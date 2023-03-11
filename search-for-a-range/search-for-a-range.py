class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if len(nums) and nums[left] == target:
            ans = len(nums)
            for i in range(left, len(nums)):
                if nums[i] == target:
                    ans = i
            return [left, ans]
        return [-1 , -1]
        