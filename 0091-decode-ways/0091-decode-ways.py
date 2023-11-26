class Solution:
    def numDecodings(self, s: str) -> int:
        if not s and len(s) == 0:
            return 0
        if len(s) and s[0] == '0':
            return 0
        prev1 = 1
        prev2 = 1
        ZERO = ord('0')
        for i in range(1, len(s)):
            curr = ord(s[i]) - ZERO
            combi = ((ord(s[i - 1]) - ZERO)* 10) + curr
            val = 0
            if curr >= 1:
                val += prev2
            if combi >= 10 and combi <= 26:
                val += prev1
            prev1 = prev2
            prev2 = val
        return prev2
                
                
            
        