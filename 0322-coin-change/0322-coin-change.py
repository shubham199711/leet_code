class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for money in range(1, amount + 1):
            for coin in coins:
                if money - coin >= 0:
                    dp[money] = min(dp[money], dp[money - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
            
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        queue = [[0,0]]
        visited = set()
        for node, step in queue:
            for coin in coins:
                if node + coin in visited: continue
                if node + coin == amount: return step + 1
                elif node + coin < amount:
                    queue.append([node + coin, step + 1 ])
                    visited.add(node + coin)
        return -1
                
                
