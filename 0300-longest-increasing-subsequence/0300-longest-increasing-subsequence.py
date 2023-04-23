class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0] * n
        ans[0] = 1
        for i in range(n):
            item = nums[i]
            runMax = 0
            for j in range(0, i):
                if nums[j] < item and runMax < ans[j]:
                    runMax = ans[j]
            ans[i] = runMax + 1
        return max(ans) 
            
                
