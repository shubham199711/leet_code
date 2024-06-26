import bisect
class MedianFinder:
    def __init__(self):
        self.numbers = []
        

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.numbers, num)
        
    def findMedian(self) -> float:
        mid = len(self.numbers) // 2
        if len(self.numbers) % 2 == 0:
            return (self.numbers[mid] + self.numbers[mid - 1]) / 2
        else:
            return self.numbers[mid]
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()