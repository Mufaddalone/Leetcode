class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or (r,c) in visited:
                return
            if grid[r][c] == 1:
                visited.add((r,c))
                dfs(r+1,c)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r,c-1)

        for i in range(m):
            if grid[i][0] == 1 and (i,0) not in visited:
                dfs(i,0)
            if grid[i][n-1] == 1 and (i,n-1) not in visited:
                dfs(i,n-1)
        
        for j in range(n):
            if grid[0][j] == 1 and (0,j) not in visited:
                dfs(0,j)
            if grid[m-1][j] == 1 or (m-1,j) not in visited:
                dfs(m-1,j)

        count =0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    count+=1
        return count
        