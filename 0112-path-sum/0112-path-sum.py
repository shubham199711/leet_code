class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root,sum - root.val)]
        while stack:
            u = stack.pop()
            if not u[0].left and not u[0].right:
                if u[1] == 0:
                    return True
            if u[0].left:
                stack.append((u[0].left, u[1]-u[0].left.val))
            if u[0].right:
                stack.append((u[0].right, u[1]-u[0].right.val))
        return False