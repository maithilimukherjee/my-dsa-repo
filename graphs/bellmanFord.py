class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [10**8] * V
        dist[src] = 0
        
        # relax edges V-1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != 10**8 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        # check negative cycle
        for u, v, w in edges:
            if dist[u] != 10**8 and dist[u] + w < dist[v]:
                return [-1]
        
        return dist
