class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(t) == len(s) and sorted(s) == sorted(t)
        