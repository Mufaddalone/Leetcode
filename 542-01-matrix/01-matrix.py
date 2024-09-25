class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        m = len(mat)
        n = len(mat[0])
        dist = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i,j,0])
                    dist[i][j] = 0
                    visited.add((i,j))
        dri = [[0,1],[1,0],[-1,0],[0,-1]]
        while q:
            r,c,dis = q.popleft()
            dist[r][c] = dis
            for dr,dc in dri:
                nr,nc = dr+r,c+dc
                if nr>=m or nc>=n or nr<0 or nc<0 or (nr,nc) in visited:
                    continue 
                q.append([nr,nc,dis+1])
                visited.add((nr, nc))
        return dist

