class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        @lru_cache(None)
        def dfs(x1, x2, k):
            ans = 0
            if k == 0:
                total = 0
                for i in range(x1, m):
                    for j in range(x2, n):
                        if pizza[i][j] == 'A':
                            total += 1
                return int(total != 0)
            sum_hor_cuts = 0
            for i in range(x1, m -1):
                for j in range(x2, n):
                    if pizza[i][j] == 'A':
                        sum_hor_cuts += 1
                if sum_hor_cuts > 0:
                    ans += dfs(i + 1, x2, k - 1)

            sum_ver_cuts = 0
            for j in range(x2, n - 1):
                for i in range(x1, m):
                    if pizza[i][j] == 'A':
                        sum_ver_cuts += 1
                if sum_ver_cuts > 0:
                    ans += dfs(x1 , j + 1, k - 1)
            return ans
        return dfs(0, 0, k -1) % (10 ** 9 + 7)