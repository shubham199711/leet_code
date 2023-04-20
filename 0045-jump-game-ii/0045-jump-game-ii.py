class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque([(0,0)])
        vis = set([0])
        while q:
            curInd,jumps = q.popleft()
            if curInd >= n-1:
                return jumps
            curDist = nums[curInd]
            for i in range(curDist,0,-1):
                if curInd+i in vis:
                    break
                else:
                    q.append((curInd+i,jumps+1))
                    vis.add(curInd+i)
        return -1