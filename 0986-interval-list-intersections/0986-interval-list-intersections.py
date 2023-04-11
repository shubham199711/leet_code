class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        pt1 , pt2 = 0 , 0
        ans = []
        while pt1 < len(firstList) and pt2 < len(secondList):
            [s1,e1] = firstList[pt1]
            [s2,e2] = secondList[pt2]
            s, e = max(s1 ,s2), min(e1, e2)
            if s <= e:
                ans.append([s, e])
            if e1 < e2:
                pt1 += 1
            else:
                pt2 += 1
        return ans 
                
                
                
        