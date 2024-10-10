class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        # indegree = [0] * numCourses
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        q = deque()
        indegree= [0]*numCourses
        for i in adj:
            for j in adj[i]:
                indegree[j] +=1
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for i in adj[node]:
                indegree[i] -=1
                if indegree[i] == 0:
                    q.append(i)
        return len(topo)== numCourses
        # q = deque()
        # for i,c in enumerate(indegree):
        #     if not c:
        #         q.append(i)
        # while q:
        #     crs = q.popleft()
        #     for pre in adj[crs]:
        #         indegree[pre] -= 1
        #         if indegree[pre] ==0:
        #             q.append(pre)
        # return True if sum(indegree) == 0 else False
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

        