class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = {}
        ans = []
        for item in nums1:
            if cache.get(item) is not None:
                cache[item] += 1
            else:
                cache[item]  = 1
        for item in nums2:
            if cache.get(item) is not None and cache[item] > 0:
                ans.append(item)
                cache[item] -= 1
        return ans
                

