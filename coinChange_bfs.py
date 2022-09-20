def coinChange(self, coins: List[int], amount: int) -> int:
    if amount == 0: return 0
    queue = [[0,0]]
    visited = set()
    for currentAmount, step in queue:
        for coin in coins:
            newCurrentAmount = currentAmount + coin
            if newCurrentAmount in visited: continue
            if newCurrentAmount == amount: return step + 1
            elif newCurrentAmount < amount:
                queue.append([newCurrentAmount, step + 1])
                visited.add(newCurrentAmount)
    return -1