class Solution:
    def rob(self, nums: List[int]) -> int:
        def basicRob(start, end):
            rob, nonRob =nums[start], 0
            for i in range(start+1, end):
                preRob, preno = rob, nonRob
                rob = preno+nums[i]
                nonRob = max(preRob, preno)
            return max(rob, nonRob)
        
        n = len(nums)
        if n<=1:
            return sum(nums)
        else:
            return max(basicRob(0, len(nums)-1), basicRob(1, len(nums)))
        