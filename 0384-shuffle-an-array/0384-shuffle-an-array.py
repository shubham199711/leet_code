class Solution:

    def __init__(self, nums: List[int]):
        self.mainNums = nums[::]
        self.workingNums = nums
        

    def reset(self) -> List[int]:
        self.workingNums = self.mainNums[::]
        return self.workingNums
        

    def shuffle(self) -> List[int]:
        n = len(self.workingNums)
        for i in range(n):
            idx = random.randint(0, n - 1)
            self.workingNums[i], self.workingNums[idx] = self.workingNums[idx], self.workingNums[i]
        return self.workingNums
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()