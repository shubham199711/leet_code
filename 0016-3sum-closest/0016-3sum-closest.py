class Solution:
    def threeSumClosest(self, nums, target):
        output =  math.inf
        nums = sorted(nums)
        
        for i in range(len(nums) -2):
            if nums[i] == nums[i-1] and i>0:
                continue
                
            left = i+1
            right = len(nums)-1
            
            while left<right:
                sum = nums[i]+nums[left]+nums[right]
                
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(output - target):
                    output = sum
                    
                if target >= sum:
                    left += 1
                    
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                else:
                    right -= 1                    
                    
        return output