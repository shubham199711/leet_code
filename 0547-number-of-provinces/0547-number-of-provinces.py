class Solution:
    def findCircleNum(self, A):
        N = len(A)
        seen = set()
        def dfs(node):
            for j, item in enumerate(A[node]):
                if item == 1 and j not in seen:
                    seen.add(j)
                    dfs(j)

        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
