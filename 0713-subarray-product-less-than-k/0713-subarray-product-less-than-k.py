class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        begin = 0
        end = 0
        cur = 1
        count = 0
        end = begin
        n = len(nums)
        while begin < n:
            while end < n and (cur*nums[end]) < k:
                cur*=nums[end]
                end+=1
            count += (end - begin)
            cur = max(cur/nums[begin], 1)  # corner case nums[begin] >= k
            begin += 1
            end = max(begin,end) # corner case nums[begin] >= k
        return count