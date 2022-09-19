def coinChange(self, coins: List[int], amount: int) -> int:
    if amount == 0: return 0
    queue = [[0,0]]
    visited = set()
    for currentAmount, step in queue:
        for coin in coins:
            if currentAmount + coin in visited: continue
            if currentAmount + coin == amount: return step + 1
            elif currentAmount + coin < amount:
                queue.append([currentAmount + coin, step + 1 ])
                visited.add(currentAmount + coin)
    return -1