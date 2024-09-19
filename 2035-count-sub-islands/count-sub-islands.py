class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n = len(grid2)
        m = len(grid2[0])
        visited = set()
        dri = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(r,c):
            if r < 0 or c < 0 or r >= n or c >= m or (r,c) in visited or grid2[r][c] == 0:
                return True
            
            visited.add((r,c))
            is_sub_island = grid1[r][c] == 1  # Check current cell
            
            for dr, dc in dri:
                nr, nc = r + dr, c + dc
                is_sub_island &= dfs(nr, nc)  # Explore all connected cells
            
            return is_sub_island
                
        count= 0
        for r in range(n):
            for c in range(m):
                if grid2[r][c] ==1 and (r,c) not in visited and dfs(r,c):
                    count+=1
        return count
