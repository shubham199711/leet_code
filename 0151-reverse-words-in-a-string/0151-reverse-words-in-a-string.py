class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x for x in s.strip().split(' ')[::-1] if len(x) > 0])
        
        