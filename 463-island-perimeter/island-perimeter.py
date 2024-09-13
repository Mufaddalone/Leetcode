class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            rowbound = len(grid)
            colbound = len(grid[0])
            if r<0 or r>=rowbound or c<0 or c>=colbound or grid[r][c] == 0: return 1
            if (r,c) in visited:return 0
            visited.add((r,c))
            peri = dfs(r,c+1)
            peri += dfs(r+1,c)
            peri += dfs(r-1,c)
            peri += dfs(r,c-1)
            return peri
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    return dfs(r,c)
        