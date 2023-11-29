class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        memo, visited = {}, set()
        def dfs(node):
            if node in visited:
                return memo[node]
            memo[node] = Node(node.val)
            visited.add(node)
            for n in node.neighbors:
                memo[node].neighbors.append(dfs(n))
            return memo[node]
        return dfs(node)
    
