class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n, frequency in collections.Counter(nums).items():
            res += [r+[n]*i for r in res for i in range(1, frequency+1)]
        return res