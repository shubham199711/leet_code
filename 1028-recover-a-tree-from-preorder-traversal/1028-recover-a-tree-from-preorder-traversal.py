# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        def getCountAndNextNumber():
            count = 0
            num = ''
            for j in range(i, len(traversal)):
                if traversal[j] != '-':
                    num += traversal[j]
                elif traversal[j] == '-' and num == '':
                    count += 1
                else:
                    break
            return (count, num)
        
        count, num = getCountAndNextNumber()
        root = TreeNode(num)
        i += count + len(num)
        
        def dfs(head, level):
            nonlocal i
            if i == len(traversal) - 1:
                return None
            count, num = getCountAndNextNumber()
            if level == count:
                if head.left is None:
                    head.left = TreeNode(num)
                    i += count + len(num)
            else:
                return
            dfs(head.left, level + 1)
            count, num = getCountAndNextNumber()
            if level == count:
                if head.right is None:
                    head.right = TreeNode(num)
                    i += count + len(num) 
            else:
                return
            dfs(head.right, level + 1)
            
        dfs(root, 1)
        return root
        