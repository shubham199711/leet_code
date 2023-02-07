import collections
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        trackingDict = {}
        for i, item in enumerate(groupSizes):
            if trackingDict.get(item) is not None:
                array = trackingDict.get(item)
                if len(array) == item:
                    ans.append(array)
                    trackingDict[item] = [i]
                else:
                    trackingDict[item].append(i)
            else:
                 trackingDict[item] = [i]
        for k,v in trackingDict.items():
            ans.append(v)
        return ans
