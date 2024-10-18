class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        dist = [[float("inf")for i in range(n)]for j in range(m)]
        q = []
        heapq.heappush(q, (0,0,0))
        dist[0][0] = 0
        dri = [[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            dis,r,c = heapq.heappop(q)
            for dr,dc in dri:
                nr,nc = r+dr,c+dc
                if nr>=0 and nc>=0 and nr<m and nc<n:
                    effort = max(abs(heights[r][c] - heights[nr][nc]),dis)
                    if effort < dist[nr][nc]:
                        dist[nr][nc] = effort
                        heapq.heappush(q,(effort,nr,nc))
        return dist[m-1][n-1]