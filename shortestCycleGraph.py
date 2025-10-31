from collections import deque

class Solution:
    def shortCycle(self, V, edges):
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        INF = 10**9
        ans = INF

        # Run BFS from each vertex
        for s in range(V):
            dist = [-1] * V
            parent = [-1] * V
            q = deque([s])
            dist[s] = 0

            while q:
                u = q.popleft()
                for v in adj[u]:
                    # Case 1: new vertex — normal BFS
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)

                    # Case 2: found a visited vertex that's not the parent
                    elif parent[u] != v:
                        cycle_len = dist[u] + dist[v] + 1
                        ans = min(ans, cycle_len)

        # No cycle found
        return -1 if ans == INF else ans
