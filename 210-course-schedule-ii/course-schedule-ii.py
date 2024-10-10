class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        if len(topo)==numCourses:
            return topo[::-1] 
        else:
            return []
                
                