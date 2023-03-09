# class CountIntervals:

#     def __init__(self):
#         self.intervals = []
#         self.total = 0
        

#     def add(self, left: int, right: int) -> None:
#         if not self.intervals:
#             self.intervals.append([left, right])
#             self.total = right - left + 1
#             return
#         def bst(item, index):
#             l, r = 0, len(self.intervals) - 1
#             while l <= r:
#                 mid = (l + r) // 2
#                 if self.intervals[mid][index] < item:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#             return l
#         l = bst(left, 0) # O(log n)
#         r = bst(right, 1) # O(log n)
#         print(f"{l = }, {r = }, {self.intervals = } {left = }, {right = }")
#         if l < len(self.intervals):
#             left = min(left, self.intervals[l][0])
            
#         if r > 0:
#             right = max(right, self.intervals[r-1][1])
        
#         to_add = right - left + 1
        
#         to_remove = 0
#         for i in range(l, r):
#             to_remove += self.intervals[i][1] - self.intervals[i][0] + 1
            
#         self.total += to_add - to_remove
#         self.intervals[l:r] = [[left, right]]

#     def count(self) -> int:
#         return self.total
    

    
    
import bisect
from operator import itemgetter

class CountIntervals:

    def __init__(self):
        self.intervals = []
        self.cur_count = 0

    def add(self, left: int, right: int) -> None:
        if not self.intervals:
            self.intervals.append([left, right])
            self.cur_count = right - left + 1
            return
        l = bisect.bisect_left(self.intervals, left, key=itemgetter(1))
        r = bisect.bisect_right(self.intervals, right, key=itemgetter(0))
        
        if l < len(self.intervals):
            left = min(left, self.intervals[l][0])
            
        if r > 0:
            right = max(right, self.intervals[r-1][1])
        
        to_add = right - left + 1
        
        to_remove = 0
        for i in range(l, r):
            to_remove += self.intervals[i][1] - self.intervals[i][0] + 1
            
        self.cur_count += to_add - to_remove
        self.intervals[l:r] = [[left, right]]

    def count(self) -> int:
        return self.cur_count


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
        


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()