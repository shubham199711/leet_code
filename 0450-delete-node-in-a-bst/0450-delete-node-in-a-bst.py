class Solution(object):
    def deleteNode(self, root, key):
        if not root:    return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            smallestNode_in_right = self.findSmallest(root.right)
            if not smallestNode_in_right:   return root.left
            smallestNode_in_right.left = root.left
            return root.right
    
    def findSmallest(self, root):
        if not root:    return None
        while root.left:
            root = root.left
        return root