class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        left = right = _max = 0
        seen = set([])
        while right < len(s):
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1
            _max = max(_max, right - left)
            if right < len(s) and s[right] in seen:
                seen.remove(s[left])
                left += 1
        return _max
