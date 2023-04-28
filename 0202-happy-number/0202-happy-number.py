class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        n = str(n)
        while True:
            ans = []
            for char in n:
                if char == '0':
                    pass
                else:
                    ans.append(int(char) ** 2)
            ans = str(sum(ans))
            if ans in seen:
                return False
            if ans == '1':
                return True
            seen.add(ans)
            n = ans
            
        