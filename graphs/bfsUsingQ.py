from collections import deque

class Solution:
    def bfs(self, adj):
        V = len(adj)
        
        visited = [False] * V
        bfs = []
        
        q = deque()
        
        # start from node 0
        q.append(0)
        visited[0] = True
        
        while q:
            node = q.popleft()
            bfs.append(node)
            
            for neighbor in adj[node]:   # maintain given order
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
        
        return bfs
