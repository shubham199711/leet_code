class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        def dfs(_target, path = []):
            if _target < 0:
                return
            if _target == 0:
                ans.add(tuple(sorted(path)))
                return
            for j in range(0, len(candidates)):
                val =  candidates[j]
                dfs(_target - val, path + [val])
        dfs(target)
        return ans
        