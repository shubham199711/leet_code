class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = [(root, sum - root.val)]
        while stack:
            head, val = stack.pop()
            if not head.left and not head.right:
                if val == 0:
                    return True
            if head.left:
                stack.append((head.left, val - head.left.val))
            if head.right:
                stack.append((head.right, val - head.right.val))
        return False