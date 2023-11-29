class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        memo= {}
        def dfs(node):
            if memo.get(node) is not None:
                return memo[node]
            memo[node] = Node(node.val)
            for n in node.neighbors:
                memo[node].neighbors.append(dfs(n))
            return memo[node]
        return dfs(node)
    
