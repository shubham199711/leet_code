class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [x + 1 for x in range(n)]
        i = 0
        while len(players) > 1:
            i = (i + k - 1) % len(players)
            players.pop(i)
        return players[0]
        
        