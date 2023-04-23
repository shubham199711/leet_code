class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def helper(s, path):
            if s == "":
                ans.append(' '.join(path))
            for w in wordDict:
                if not s.startswith(w):  continue
                path.append(w)
                helper(s[len(w):], path)
                path.pop()
        helper(s, [])
        return ans
        