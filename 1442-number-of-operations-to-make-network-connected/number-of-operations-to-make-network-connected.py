class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]
        size = [0] *(n+1)
        extra = 0
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
        
        for u,v in connections:
            if find(u) == find(v):
                extra+=1
            else:
                union(u,v)
        
        count=0
        for i in range(n):
            if i == parent[i]:
                count+=1
        ans = count-1
        if extra >= ans:
            return ans
        else:
            return -1
