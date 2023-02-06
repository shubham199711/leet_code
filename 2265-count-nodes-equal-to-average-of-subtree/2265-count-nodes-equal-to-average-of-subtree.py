# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count=0
        def dfs(node):
            if(not node):
                return [0,0]
            left=dfs(node.left)
            right=dfs(node.right)
            left_sum,left_count=left[0],left[1]
            right_sum,right_count=right[0],right[1]
            tot=node.val+left_sum+right_sum
            if(node.val==tot//(1+left_count+right_count)):
                self.count+=1
            return [tot,1+left_count+right_count]
        dfs(root)
        return self.count
        