# remember: revisited node must not be the parent node.
if you see any already visited node that is not your parent, it means you found another path back to that node → cycle!

class Solution:
    def isCycle(self, V, edges):
        # build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * V
        
        # dfs helper function
        def dfs(node, parent):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    if dfs(nei, node):   # recurse deeper
                        return True
                elif nei != parent:      # visited and not parent => cycle
                    return True
            return False
        
        # run dfs for every component
        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True
                    
        return False
