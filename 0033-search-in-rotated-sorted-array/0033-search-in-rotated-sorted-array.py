class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            midNum = nums[mid]

            if midNum == target:
                return mid

            if midNum >= nums[left]:
                if target < nums[left] or midNum < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] or midNum > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1