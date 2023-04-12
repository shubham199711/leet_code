class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        ans = []
        for i in range(len(s) - len(p) + 1):
            _s = sorted(s[i:i + len(p)])
            if p == _s:
                ans.append(i)
        return ans
        