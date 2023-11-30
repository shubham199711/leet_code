class Solution(object):
    def singleNumber(self, nums):
        ret = 0
        for i in range(32):
            if sum((n>>i)&1 for n in nums) % 3:
                if i == 31:
                    ret -= 2**31
                else:
                    ret += (1<<i)
        return ret