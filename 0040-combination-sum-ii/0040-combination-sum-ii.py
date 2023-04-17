# use dfs in combinations problem's
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(current_total, idx = 0, path=[]):
            if current_total < 0:
                return
            if current_total == 0:
                ans.append(path)
                return
            for i in range(idx, len(candidates)):
                val = candidates[i]
                if idx != i and val == candidates[i-1]: continue  # if not the same first element and same as last element
                dfs(current_total-val, i+1, path+[val])
        dfs(target)
        return ans