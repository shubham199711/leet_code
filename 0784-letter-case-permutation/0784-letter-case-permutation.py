class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        m = len(s)
        ans = []
        
        def dfs(i, listOfChar):
            if len(listOfChar) == m:
                return ans.append(''.join(listOfChar))
            if ord('0') <= ord(s[i]) <= ord('9'):
                _list = listOfChar.copy()
                _list.append(s[i])
                dfs(i + 1, _list)
            else:
                _list = listOfChar.copy()
                _list2 = listOfChar.copy()
                _list.append(s[i].upper())
                _list2.append(s[i].lower())
                dfs(i + 1, _list)
                dfs(i + 1, _list2)
                
            
        dfs(0, [])
        return ans
        