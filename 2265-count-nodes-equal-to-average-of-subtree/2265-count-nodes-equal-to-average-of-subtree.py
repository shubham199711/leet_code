# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        _ans = 0
        runningSum = 0
        runningCount = 0
        cache = {}
        def sumAndCount(_head):
            nonlocal runningSum, runningCount, cache
            if _head is None:
                return 0, 1
            if cache.get(id(_head)) is not None:
                runningSum += cache[id(_head)][0]
                runningCount += cache[id(_head)][1]
                return runningSum, runningCount
            runningSum += _head.val
            runningCount += 1
            sumAndCount(_head.left)
            sumAndCount(_head.right)
            cache[id(_head)] = runningSum, runningCount
            return runningSum, runningCount
            
        
        def dfs(head):
            nonlocal _ans, runningSum, runningCount, cache
            if head is None:
                return 
            dfs(head.left)
            dfs(head.right)
            runningSum, runningCount = 0 , 0
            currentVal,currentCount = sumAndCount(head)
            if (currentVal // currentCount) == head.val:
                _ans += 1
            # print(f'{head.val = }, {currentVal = }, {currentCount = }, {_ans = }, {cache = }')
                
        dfs(root)
        return _ans
        