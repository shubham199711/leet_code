class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i ,item in enumerate(s):
            setOfChar = set([item])
            j = i + 1
            while j < len(s):
                if s[j] not in setOfChar:
                    setOfChar.add(s[j])
                else:
                    break
                j += 1
            ans = max(ans, len(setOfChar))
        return ans
                    
            
