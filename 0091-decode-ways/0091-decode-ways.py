class Solution:
    def numDecodings(self, s: str) -> int:
        if not s and len(s) == 0:
            return 0
        if len(s) and s[0] == '0':
            return 0
        val1 = val2 = 1
        ZERO = ord('0')
        for i in range(1, len(s)):
            curr = ord(s[i]) - ZERO
            prev = (ord(s[i - 1]) - ZERO) * 10 + curr
            val = 0
            if curr >= 1:
                val += val2
            if prev >= 10 and prev <= 26:
                val += val1
            val1 = val2
            val2 = val
        return val2
                
            