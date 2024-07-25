class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj ={ i:[] for i in range(n)}
        for par, child in edges:
            adj[par].append(child)
            adj[child].append(par)
        visited = set()

        def dfs(node):
            time = 0
            if node in visited: return 0
            visited.add(node)
            for child in adj[node]:
                time += dfs(child)
            if (time >0 or hasApple[node]) and node !=0:
                time += 2
            return time
        return dfs(0)


