class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     try:
    #         return nums.index(target)
    #     except:
    #         return -1
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        