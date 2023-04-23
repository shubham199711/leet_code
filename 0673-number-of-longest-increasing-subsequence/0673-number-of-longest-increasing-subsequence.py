class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        mem={}
        def dfs(i,p):
            if (i,p) in mem: return mem[(i,p)]
            if i==len(nums): return 0,1

            elif p==None or nums[i]>p:
                x,c1=dfs(i+1,nums[i])
                x+=1
                y,c2=dfs(i+1,p)

                if x==y: mem[(i,p)]=(x,c1+c2); return mem[(i,p)]
                elif x>y: mem[(i,p)]=(x,c1); return mem[(i,p)]
                else: mem[(i,p)]=(y,c2); return mem[(i,p)]

            else:
                mem[(i,p)]=dfs(i+1,p)
                return mem[(i,p)]

        return dfs(0,None)[1] 