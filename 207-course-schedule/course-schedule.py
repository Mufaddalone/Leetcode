class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Initialize data structures
        adj_list = defaultdict(list)
        indegrees = [0] * numCourses

        # 2. Build the graph
        for a, b in prerequisites:
            indegrees[a] += 1
            adj_list[b].append(a)

        # 3. Initialize queue with courses having no prerequisites
        q = deque()
        for i, c in enumerate(indegrees):
            if not c:
                q.append(i)

        # 4. Perform topological sorting
        while q:
            c = q.popleft()
            for n in adj_list[c]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    q.append(n)

        # 5. Check if all courses can be taken
        return True if sum(indegrees) == 0 else False
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

        