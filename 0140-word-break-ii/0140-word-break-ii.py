class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        @lru_cache(None)
        def helper(s, path):
            if s == "":
                ans.append(path)
            for w in wordDict:
                if not s.startswith(w):  continue
                helper(s[len(w):], f'{path} {w}' if len(path) else w)
        helper(s, "")
        return ans
        