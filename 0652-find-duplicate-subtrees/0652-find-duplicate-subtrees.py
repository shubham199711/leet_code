# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        def to_string(root):
            if root is None:    
                return "None"
            key = \
                "(left=" + to_string(root.left) + \
                ",right=" + to_string(root.right) + \
                ",root=" + str(root.val) + ")"
            trees[key].append(root)
            return key

        trees = collections.defaultdict(list) # default list is []
        to_string(root)

        return [roots[0] for roots in trees.values() if len(roots)>1]
        