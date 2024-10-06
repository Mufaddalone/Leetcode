class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        visit = [0]*(numCourses)
        path = [0]*(numCourses)
        result=[]
        def dfs(i):
            visit[i] = 1
            path[i] = 1
            for j in adj[i]:
                if not visit[j]:
                    if dfs(j):
                        return True
                elif path[j]:
                    return True
            path[i] = 0  # Remove from current DFS path
            visit[i] = 2  # Mark as fully processed (visited)
            result.append(i)  # Add course to result in topological order
            return False
        for i in range(numCourses):
            if visit[i] == 0:
                if dfs(i):
                    return []
        return result
                
                