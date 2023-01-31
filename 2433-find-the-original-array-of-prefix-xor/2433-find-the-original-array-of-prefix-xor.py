class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        for i,item in enumerate(pref):
            if i == 0:
                ans.append(item)
                continue
            ans.append(pref[i -1] ^ item)
        return ans
                
        