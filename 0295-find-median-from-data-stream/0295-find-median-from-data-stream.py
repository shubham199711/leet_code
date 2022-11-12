class MedianFinder:

    def __init__(self):
        self.median = None
        self.numbers = []
        

    def addNum(self, num: int) -> None:
        self.numbers.append(num)
        
    def findMedian(self) -> float:
        self.numbers.sort()
        mid = len(self.numbers) // 2
        if len(self.numbers) % 2 == 1:
            return self.numbers[mid]
        else:
            return (self.numbers[mid] + self.numbers[mid - 1]) / 2
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()