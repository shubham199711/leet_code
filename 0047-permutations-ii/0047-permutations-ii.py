class Solution:
    def permutations(self,cur,idx,ans):
        if idx==len(cur):
            ans.append(cur[::])
        if idx>=len(cur):return 
        seen = set()
        for i in range(idx,len(cur)):
            if cur[i] not in seen:
                seen.add(cur[i])
                cur[i],cur[idx]=cur[idx],cur[i]
                self.permutations(cur,idx+1,ans)
                cur[i],cur[idx]=cur[idx],cur[i]
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        self.permutations(nums,0,ans)
        return ans