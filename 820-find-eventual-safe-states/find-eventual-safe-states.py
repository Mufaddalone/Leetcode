class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        m = len(graph)
        safe = []
        visit = [0]*(m)
        path = [0]*(m)
        check = [0]*(m)
        def dfs(i):
            visit[i] = 1
            path[i] = 1
            for j in graph[i]:
                if not visit[j]:
                    if dfs(j):
                        return True
                elif path[j]:
                    return True
            path[i] = 0  
            check[i] = 1
            return False
        for i in range(m):
            if visit[i] == 0:
                dfs(i)
        for i in range(m):
            if check[i] ==1:
                safe.append(i)
        return safe