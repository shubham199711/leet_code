class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        i ,r = 0 , len(nums) -1
        _len = len(nums)
        while i < r:
            if nums[i] == nums[i + 1]:
                count += 1
                del nums[i + 1]
                r -= 1
            else:
                i += 1
        for i in range(count + 1):
            nums.append(-1)
        return _len - count
            
        
