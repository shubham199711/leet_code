import bisect
class Solution2:
    def kClosest(self, points, k):
        _distanceList = []
        for i,item in enumerate(points):
            distance = item[0] * item[0] + item[1] * item[1]
            bisect.insort(_distanceList, [distance, i], key = lambda x: x[0])  # type: ignore
        return [points[_distanceList[x][1]] for x in range(0, k)]


# faster
import heapq
class Solution:
    def kClosest(self, points, k: int):
        return heapq.nsmallest(k, points, lambda p: p[0] * p[0] + p[1] * p[1])