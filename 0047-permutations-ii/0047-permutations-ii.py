class Solution:
    def permutations(self,cur,idx,ans):
        if idx==len(cur):
            ans.append([x for x in cur])
        if idx>=len(cur):return 
        count=[0]*21
        for i in range(idx,len(cur)):
            if count[cur[i]-10]==0:
                count[cur[i]-10]=1
                cur[i],cur[idx]=cur[idx],cur[i]
                self.permutations(cur,idx+1,ans)
                cur[i],cur[idx]=cur[idx],cur[i]
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        self.permutations(nums,0,ans)
        return ans