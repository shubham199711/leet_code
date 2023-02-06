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
        def sumAndCount(_head, count = 0, _sum = 0):
            nonlocal runningSum, runningCount
            if _head is None:
                return 0, 1
            runningSum += _head.val
            runningCount += 1
            sumAndCount(_head.left)
            sumAndCount(_head.right)
            return runningSum, runningCount
            
        
        def dfs(head):
            nonlocal _ans, runningSum, runningCount
            if head is None:
                return 
            dfs(head.left)
            dfs(head.right)
            runningSum, runningCount = 0 , 0
            currentVal,currentCount = sumAndCount(head)
            if (currentVal // currentCount) == head.val:
                _ans += 1
            # print(f'{head.val = }, {currentVal = }, {currentCount = }, {_ans = }')
                
        dfs(root)
        return _ans
        