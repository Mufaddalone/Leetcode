class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        dri = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = set()
        island = 0
        n = len(grid)
        m = len(grid[0])
        def dfs(r,c):
            if (r<0 or c<0 or r>=n or c>=m or grid[r][c] == "0" or (r,c) in visited):
                return False
            visited.add((r,c))
            for dr,dc in dri:
                nr,nc = r+dr,c+dc
                dfs(nr,nc)
            return True
        for r in range(n):
            for c in range(m):
                if dfs(r,c):
                    island+=1
        return island