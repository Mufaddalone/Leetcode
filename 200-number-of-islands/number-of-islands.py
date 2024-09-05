class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def explore(r, c, visited, grid):
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == "0" or (r, c) in visited):
                return False
            
            visited.add((r, c))
            
            explore(r+1, c, visited, grid)
            explore(r-1, c, visited, grid)
            explore(r, c+1, visited, grid)
            explore(r, c-1, visited, grid)
            
            return True

        for r in range(rows):
            for c in range(cols):
                if explore(r, c, visited, grid):
                    islands += 1

        return islands