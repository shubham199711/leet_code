# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import bisect
class Solution:
    # with sorted array
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sortedAns = []
        sumAns = []
        def btsInPleace(head):
            if not head:
                return
            bisect.insort(sortedAns, head.val)
            btsInPleace(head.left)
            btsInPleace(head.right)
        def sumArray():
            runningSum = 0
            for i, item in enumerate(sortedAns[::-1]):
                runningSum += item
                sumAns.append(runningSum)
                
        def btsInPleaceAndUpdate(head):
            if not head:
                return
            index = bisect.bisect(sortedAns, head.val)
            head.val = sumAns[-index]
            btsInPleaceAndUpdate(head.left)
            btsInPleaceAndUpdate(head.right)
        
        btsInPleace(root)
        sumArray()
        btsInPleaceAndUpdate(root)
        return root
                
            
            
        