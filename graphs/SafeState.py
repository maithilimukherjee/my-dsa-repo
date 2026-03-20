class Solution:
    def safeNodes(self, V, edges):
        from collections import defaultdict
        
        # Step 1: Build adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        vis = [0] * V       # visited
        pathVis = [0] * V   # path visited (for cycle detection)
        safe = [0] * V      # 1 if node is safe

        # Step 2: DFS function
        def dfs(node):
            vis[node] = 1
            pathVis[node] = 1

            for nei in adj[node]:
                # unvisited neighbor
                if not vis[nei]:
                    if dfs(nei):      # if cycle found
                        return True
                # neighbor already in recursion stack
                elif pathVis[nei]:
                    return True

            # no cycle found from this node
            pathVis[node] = 0
            safe[node] = 1
            return False

        # Step 3: Call DFS for all nodes
        for i in range(V):
            if not vis[i]:
                dfs(i)

        # Step 4: Collect and return safe nodes
        ans = [i for i in range(V) if safe[i] == 1]
        return ans
