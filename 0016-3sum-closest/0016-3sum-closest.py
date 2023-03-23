class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        d, ans = float("inf"), 0
        for i in range(len(nums) - 2):
            s, e = i + 1, len(nums) - 1
            while(s < e):
                sum = nums[i] + nums[s] + nums[e]
                if sum == target: return sum
                if abs(sum - target) < d:
                    d = abs(sum - target)
                    ans = sum
                if sum < target: s += 1
                else: e -= 1
        
        return ans