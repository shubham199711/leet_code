def constructMaximumBinaryTree(self, nums):
    if nums:
        max_idx, max_val = max(enumerate(nums), key=lambda x: x[1])
        return TreeNode(max_val, self.constructMaximumBinaryTree(nums[:max_idx]), self.constructMaximumBinaryTree(nums[max_idx+1:]))