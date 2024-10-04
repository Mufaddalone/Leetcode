class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat[0])  # Number of columns
        m = len(mat)     # Number of rows
        q = deque()
        dist = [[-1] * n for _ in range(m)]  # Initialize with -1 indicating unvisited
        
        # Enqueue all the '0' cells and set their distances to 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j, 0))  # Append (i, j, distance=0)
                    dist[i][j] = 0  # Distance to itself is 0
        
        # Directions for moving up, down, left, and right
        dri = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        # BFS traversal
        while q:
            r, c, dis = q.popleft()
            
            # Explore the 4 neighboring cells
            for dr, dc in dri:
                nr, nc = r + dr, c + dc
                
                # Check if the new position is within bounds and hasn't been visited
                if 0 <= nr < m and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dis + 1  # Update distance
                    q.append((nr, nc, dis + 1))  # Enqueue the neighbor
        
        return dist
            
            