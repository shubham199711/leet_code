class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        _len = (len(graph) -1)
        ans = []
        def dfs(index,path):
            if _len  == index:
                ans.append(path)
                return
            for item in graph[index]:
                dfs(item, path + [item])
        dfs(0, [0])
        return ans
        