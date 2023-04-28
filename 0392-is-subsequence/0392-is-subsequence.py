class Solution:
    def isSubsequence(self, s, t):
        dp = [-2]*(len(s)+1)
        dp[0] =-1
        for i in range(1,len(dp)):
            if dp[i-1] == -2: return False
            for j in range(dp[i-1]+1, len(t)):
                if t[j] == s[i-1]:
                    dp[i] = j
                    break;
        return True if dp[-1] !=-2 else False