class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        dist = [[float("inf")for i in range(n)]for j in range(m)]
        dist[0][0] = 0
        q.append((1,0,0))
        dri = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        if n==1 and m==1 and grid[0][0]==0:
            return 1
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1
        while q:
            dis, r, c = q.popleft()
            for dr,dc in dri:
                nr,nc = r+dr,c+dc
                if (nr>=0 and nc>=0 and nr<m and nc<n and 1+ dis < dist[nr][nc] and grid[nr][nc] == 0):
                    dist[nr][nc] = 1+ dis
                    if (nr==m-1 and nc==n-1):
                        return dis+1
                    q.append((dis+1,nr,nc))
        return -1

            

        