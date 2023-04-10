class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # keep track of the smallest 1st and 2nd element in triplet
        # if there exist a 3rd element, return True.
        l, r = float('inf'), float('inf')
              
        for n in nums:
            if n == l or n == r:
                continue
            if n < l:
                l = n
            elif n < r:
                r = n
            else:
                return True
        return False