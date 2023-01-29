class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmeticSeq(items):
            if len(items) < 2:
                return False
            items = sorted(items, reverse=True)
            diff = items[0] - items[1]
            for i in range(0, len(items) -1):
                if (items[i] - items[i + 1]) == diff:
                    pass
                else:
                    return False
            return True
        ans = []
        for i,j in zip(l,r):
            items = nums[i:j + 1]
            ans.append(isArithmeticSeq(items))
        return ans
            
            
        