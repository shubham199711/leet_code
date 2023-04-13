class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        ans = []
        indexMap = {}
        for item in arr:
            sor = ''.join(sorted(item))
            if indexMap.get(sor) is not None:
                ans[indexMap[sor]].append(item)
            else:
                ans.append([item])
                indexMap[sor] = len(ans) - 1
        return ans
                
