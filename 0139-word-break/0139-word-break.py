from collections import deque
class Solution:
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        q = [s]
        seen = set()
        while len(q):
            s = q.pop(0)
            for item in wordDict:
                if not s.startswith(item): 
                    continue
                _s = s[len(item):]
                if _s == "": 
                    return True
                if _s not in seen:
                    seen.add(_s)
                    q.append(_s)
        return False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        dp = [False] * (m + 1)
        dp[m] = True
        for i in range(m - 1, -1, -1):
            for w in wordDict:
                s_word_len = i + len(w)
                if s_word_len <= m and s[i: s_word_len] == w:
                    dp[i] = dp[s_word_len]
                if dp[i]:
                    break
        return dp[0]
    
    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        def helper(s, path):
            if s == "":
                return True
            for w in wordDict:
                if not s.startswith(w):  continue
                path.append(w)
                if helper(s[len(w):], path):
                    return True
                path.pop()
            return False
        return helper(s, [])
