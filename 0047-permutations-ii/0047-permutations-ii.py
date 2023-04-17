class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def permutations(idx):
            if idx==len(nums):
                ans.append(nums[::])
            seen = set()
            for i in range(idx,len(nums)):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    nums[i],nums[idx]=nums[idx],nums[i]
                    permutations(idx+1)
                    nums[i],nums[idx]=nums[idx],nums[i]
        permutations(0)
        return ans