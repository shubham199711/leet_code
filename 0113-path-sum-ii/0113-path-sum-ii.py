class Solution:
    def traverse(self,node,target,current,path,ans):
        if node:
            if not node.left and not node.right:
                if node.val+current==target:
                    path.append(node.val)
                    ans.append([x for x in path])
                    path.pop()
                return 
            path.append(node.val)
            self.traverse(node.left,target,current+node.val,path,ans)
            path.pop()
            path.append(node.val)
            self.traverse(node.right,target,current+node.val,path,ans)
            path.pop()
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:return []
        ans=[]
        self.traverse(root,targetSum,0,[],ans)
        return ans