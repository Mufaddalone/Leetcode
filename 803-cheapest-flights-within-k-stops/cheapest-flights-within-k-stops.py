class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # m = len(heights)
        # n = len(heights[0])
        adj = defaultdict(list)
        for i in flights:
            adj[i[0]].append((i[1],i[2]))
        q = deque()
        dist = [float("inf")]*n
        dist[src] = 0
        q.append((0,src,0))
        while q:
            stops,node,dis = q.popleft()
            if stops>k:continue
            for adjnode,weight in adj[node]:
                if (dis + weight < dist[adjnode] and stops<=k):
                    dist[adjnode] = dis + weight
                    q.append((stops+1,adjnode,dis + weight))
        if dist[dst] == float("inf"): return -1
        return dist[dst]

                
            

        # dist = [[float("inf")for i in range(n)]for j in range(m)]
        # q = []
        # heapq.heappush(q, (0,0,0))
        # dist[0][0] = 0
        # dri = [[0,1],[1,0],[-1,0],[0,-1]]
        # while q:
        #     dis,r,c = heapq.heappop(q)
        #     for dr,dc in dri:
        #         nr,nc = r+dr,c+dc
        #         if nr>=0 and nc>=0 and nr<m and nc<n:
        #             effort = max(abs(heights[r][c] - heights[nr][nc]),dis)
        #             if effort < dist[nr][nc]:
        #                 dist[nr][nc] = effort
        #                 heapq.heappush(q,(effort,nr,nc))
        # return dist[m-1][n-1]