from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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
        
