class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = []
        last = 0
        for item in pref:
            ans.append(last ^ item)
            last = item
        return ans
                
        