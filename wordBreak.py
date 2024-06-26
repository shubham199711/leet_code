from collections import deque
def wordBreak(s: str, wordDict):
    q = deque([s])
    seen = set()
    while q:
        s = q.popleft()
        for word in wordDict:
            if s.startswith(word):
                new_s = s[len(word):]
                if new_s == "": 
                    return True
                if new_s not in seen:
                    q.append(new_s)
                    seen.add(new_s)
    return False

print(wordBreak('aaaaaaa', ['aaa', 'aaaa']))