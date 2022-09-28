# true if two `distinct` index i != j in array such as `nums[i] == nums[j]`
# and abs(i - j) <= k
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if seen.get(num) is not None:
                for j in seen[num]:
                    if abs(i - j) <= k:
                        return True
                seen[num].append(i)
            else:
                seen[num] = [i] 
        return False
        