class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveStack = []
        negetiveStack = []
        ans = []
        for item in nums:
            if item < 0:
                negetiveStack.append(item)
            else:
                positiveStack.append(item)
        for i in range(len(positiveStack)):
            ans.append(positiveStack[i])
            ans.append(negetiveStack[i])
        return ans
        