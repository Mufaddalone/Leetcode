class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = [i for i in range(n*n)]
        size = [1]*(n*n)

        def find(node):
            if node == parent[node]:
                return node
            parent[node] = find(parent[node])
            return parent[node]

        def union(u,v):
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return
            if size[root_u] > size[root_v]:
                size[root_u] += size[root_v]
                parent[root_v] = root_u
            else:
                size[root_v] += size[root_u]
                parent[root_u] = root_v

        dri =[[0,1],[1,0],[-1,0],[0,-1]]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                for dr,dc in dri:
                    nr,nc = r+dr,dc+c
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 1:
                        node = (r*n)+c
                        adjnode = (nr*n)+nc
                        union(node,adjnode)
        maxs = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    continue
                z = set()
                for dr,dc in dri:
                    nr,nc = r+dr,dc+c
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 1:
                        z.add(find((nr*n)+nc))
                sizetotal = 0
                for i in z:
                    sizetotal += size[i] 
                maxs = max(maxs,sizetotal+1)

        for i in range(n*n):
            maxs = max(maxs,size[find(i)])
        return maxs


                
        