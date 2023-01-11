# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum_OLD(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxLevel = 0
        levelValueObj = {}
        def setMaxLevelOfTree(root: Optional[TreeNode], runningLevel: int) -> None:
            nonlocal maxLevel
            nonlocal levelValueObj
            if root is not None:
                maxLevel = max(maxLevel, runningLevel)
                if levelValueObj.get(runningLevel) is not None:
                    levelValueObj[runningLevel].append(root.val)
                else:
                    levelValueObj[runningLevel] = [root.val]
                setMaxLevelOfTree(root.left, runningLevel + 1)
                setMaxLevelOfTree(root.right, runningLevel + 1)
        setMaxLevelOfTree(root, 0)
        return sum(levelValueObj[maxLevel])
    
    # use less memory
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxLevel = 0
        ans = 0
        def dfs(root = root, runningLevel = 0) -> None:
            nonlocal maxLevel
            nonlocal ans
            if root is not None:
                dfs(root.left, runningLevel + 1)
                dfs(root.right, runningLevel + 1)
                if maxLevel < runningLevel:
                    ans = 0
                    maxLevel = runningLevel
                if maxLevel == runningLevel:
                    ans += root.val
        dfs()
        return ans

