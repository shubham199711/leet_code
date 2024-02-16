class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l,r,_max = 0, 0, 0
        seen = set([])
        while r < len(s):
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1 
            _max = max(_max, r - l)
            if r < len(s) and s[r] in seen:
                seen.remove(s[l])
                l += 1
        return _max
              
        
