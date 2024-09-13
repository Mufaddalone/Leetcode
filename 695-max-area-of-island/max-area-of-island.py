class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
           
        def dfs(r,c):
            if (r<0 or c<0 or r>=len(grid) or c>= len(grid[0]) or grid[r][c]==0 or (r, c) in visited):
                return 0
            visited.add((r,c))
            size =1
            size += dfs(r,c+1)
            size += dfs(r+1,c)
            size += dfs(r,c-1)
            size += dfs(r-1,c)
            return size

        maxsize = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = dfs(r,c)
                if (size>0 and size>maxsize):
                    maxsize= size
        return maxsize
     