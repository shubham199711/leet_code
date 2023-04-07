class Solution:
    def sortColors(self, nums: List[int]) -> None:
        idx=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                nums[i]=nums[idx]
                nums[idx]=0
                idx+=1
        for i in range(idx,n):
            if nums[i]==1:
                nums[i]=nums[idx]
                nums[idx]=1
                idx+=1