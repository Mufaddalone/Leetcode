class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
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

        max_row= 0
        max_col = 0
        for i in stones:
            max_row = max(max_row,i[0])
            max_col = max(max_col,i[1])
        n = max_row + max_col +1
        parent = [i for i in range(n+1)]
        size = [0]*(n+1)
        stonedge = {}
        count = 0
        for i in stones:
            row = i[0]
            col = i[1] + max_row + 1
            stonedge[row] = 1
            stonedge[col] = 1
            union(row,col)
        for i in stonedge:
            if (find(i) == i):
                count+=1
        return len(stones)-count


        





        # max_row = 0
        # max_col = 0
        # for i in stones:
        #     max_row = max(max_row,i[0])
        #     max_col = max(max_col,i[1])
        # stoneNodes = {}
        # n = max_row + max_col +1
        # parent = [i for i in range(n+1)]
        # size = [0]*(n+1)
        # for i in stones:
        #     row = i[0]
        #     col = i[1] + max_row +1
        #     union(row,col)
        #     stoneNodes[row] = 1
        #     stoneNodes[col] = 1
        # count = 0
        # for i in stoneNodes:
        #     if (find(i) == i):
        #         count+=1
        # return len(stones) - count


