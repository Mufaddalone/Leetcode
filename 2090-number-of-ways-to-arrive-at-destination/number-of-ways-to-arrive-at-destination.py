class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        dist = [float("inf")]*n
        ways = [0]*n
        adj = defaultdict(list)
        for i in roads:
            adj[i[0]].append((i[1],i[2]))
            adj[i[1]].append((i[0],i[2]))
        q = []
        dist[0] = 0
        ways[0] = 1
        heapq.heappush(q,(0,0))
        mod = 1e9+7
        while q:
            dis , node = heapq.heappop(q)
            for adjnode, weight in adj[node]:
                if dis + weight < dist[adjnode]:
                    dist[adjnode] = dis + weight
                    heapq.heappush(q,(dist[adjnode],adjnode))
                    ways[adjnode] = ways[node]
                elif dis + weight == dist[adjnode]:
                    ways[adjnode] = (ways[adjnode] + ways[node])%mod
        return int(ways[-1]%mod)
