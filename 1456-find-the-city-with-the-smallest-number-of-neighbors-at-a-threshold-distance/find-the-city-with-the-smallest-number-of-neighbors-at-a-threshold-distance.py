class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))

        def dijkstra(start):
            dist = [float("inf")]*n
            dist[start] = 0
            q = [(0,start)]
            while q:
                d,node = heappop(q)
                if d>dist[node]:
                    continue 
                for neighbour,weight in adj[node]:
                    if d+weight<dist[neighbour]:
                        dist[neighbour] =  d+weight
                        heappush(q,(d+weight,neighbour) )   
            return sum(1 for i in range(n) if dist[i] <= distanceThreshold)

        min_neighbors = n
        result_city = -1
    
        for city in range(n):
            reachable = dijkstra(city)
            if reachable < min_neighbors or (reachable == min_neighbors and city > result_city):
                min_neighbors = reachable
                result_city = city
        
        return result_city 
