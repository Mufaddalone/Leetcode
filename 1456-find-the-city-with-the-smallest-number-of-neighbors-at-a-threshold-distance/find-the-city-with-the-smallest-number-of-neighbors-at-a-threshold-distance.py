class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))

        def dj(src):
            dist = [float("inf")]*n
            dist[src] = 0
            q = []
            heapq.heappush(q,(0,src))
            while q:
                dis , node = heapq.heappop(q)
                for adjnode, weight in adj[node]:
                    if dis + weight < dist[adjnode]:
                        dist[adjnode] = dis + weight
                        heapq.heappush(q,(dist[adjnode],adjnode))
            a = 0
            for i in range(n):
                if dist[i] <= distanceThreshold:
                    a+=1
            return a
        cityno = -1
        cntcity = n
        for i in range(n):
            cnt = dj(i)
            if cnt <= cntcity:
                cntcity = cnt
                cityno = i
        return cityno
                

