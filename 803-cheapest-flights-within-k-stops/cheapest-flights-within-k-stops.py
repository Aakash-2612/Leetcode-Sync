from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        heap = [(0, src, 0)] # cost, node, stops

        while heap:
            cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            for nei, weight in graph[node]:
                new_cost = cost + weight

                if new_cost < dist[nei][stops + 1]:
                    dist[nei][stops + 1] = new_cost
                    heapq.heappush(heap, (new_cost, nei, stops + 1))
        
        return -1
