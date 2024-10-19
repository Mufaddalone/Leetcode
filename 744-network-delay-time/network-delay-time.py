class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")]*(n+1)
        adj = defaultdict(list)
        for i in times:
            adj[i[0]].append((i[1],i[2]))
        q = []
        dist[k]=0
        heapq.heappush(q,(0,k))
        while q:
            dis, node = heapq.heappop(q)
            for adjnode,weight in adj[node]:
                if dis + weight < dist[adjnode]:
                    dist[adjnode] = dis+weight
                    heapq.heappush(q,(dist[adjnode],adjnode))
        max_dist = max(dist[1:])
        return max_dist if max_dist != float("inf") else -1
                