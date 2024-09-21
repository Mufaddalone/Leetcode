class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for crs ,pre in prerequisites:
            indegree[crs] +=1
            adj[pre].append(crs)

        q = deque()
        for i,c in enumerate(indegree):
            if not c:
                q.append(i)
        
        while q:
            crs = q.popleft()
            for pre in adj[crs]:
                indegree[pre] -= 1
                if indegree[pre]==0:
                    q.append(pre)
        return True if sum(indegree)==0 else False
        # adj = {i :[] for i in range(numCourses)}

        # for crs , pre in prerequisites:
        #     adj[crs].append(pre)

        # visited = set()

        # def dfs(crs):
        #     if crs in visited:
        #         return False
        #     if adj[crs] == []:
        #         return True
        #     visited.add(crs)
        #     for pre in adj[crs]:
        #         if not dfs(pre): return False
        #     visited.remove(crs)
        #     adj[crs] = []
        #     return True
        # for crs in range(numCourses):
        #     if not dfs(crs):return False
        # return True

        