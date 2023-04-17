class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def permutations(i):
            if i == len(nums):
                ans.append(nums[::])
            seen = set()
            for j in range(i, len(nums)):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    nums[j],nums[i]=nums[i],nums[j]
                    permutations(i+1)
                    nums[j],nums[i]=nums[i],nums[j]
        permutations(0)
        return ans