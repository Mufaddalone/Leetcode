class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        n = len(grid)
        m = len(grid[0])
        dri = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(r,c):
            if r<0 or c<0 or r>=n or c>=m or grid[r][c]==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            size = 1
            for dr,dc in dri:
                nr,nc = r+dr,c+dc
                size+= dfs(nr,nc)
            return size
        maxsize =0
        for r in range(n):
            for c in range(m):
                size = dfs(r,c)
                if (size>maxsize):
                    maxsize = size
        return maxsize
                
