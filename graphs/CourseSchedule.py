# -------------------------------------------------------
# Question: Course Schedule II
# -------------------------------------------------------
# You are given n courses labeled from 0 to n - 1 and a 
# list of prerequisite pairs where prerequisites[i] = [x, y]
# means you must take course y before taking course x.
#
# You need to return one possible ordering of courses such 
# that all courses can be completed.
# If it's impossible (due to cyclic dependencies), 
# return an empty list.
#
# Example:
# Input: n = 3, prerequisites = [[1, 0], [2, 1]]
# Output: [0, 1, 2]
# -------------------------------------------------------


# -------------------------------------------------------
# Trick:
# -------------------------------------------------------
# Whenever you see dependencies like "A before B" or
# "to do X, first complete Y", it's a Directed Acyclic Graph (DAG)
# problem → solved using Topological Sort.
#
# If a valid topological order exists → all tasks can be completed.
# If a cycle exists → no valid order → return [].
# -------------------------------------------------------


# -------------------------------------------------------
# Logic Followed:
# -------------------------------------------------------
# 1️⃣ Represent the courses as a directed graph using adjacency list.
# 2️⃣ Calculate the indegree (number of incoming edges) of each node.
# 3️⃣ Start with all nodes having indegree 0 (no prerequisites).
# 4️⃣ Use BFS (Kahn’s Algorithm):
#     - Pick nodes with indegree 0.
#     - Add to result list (topological order).
#     - Reduce indegree of their neighbors by 1.
#     - If any neighbor’s indegree becomes 0, push to queue.
# 5️⃣ If we processed all nodes → return topo order.
#     Else → cycle detected → return empty list.
# -------------------------------------------------------


# -------------------------------------------------------
# Steps (Implementation using Kahn’s Algorithm)
# -------------------------------------------------------
from collections import deque

class Solution:
    def findOrder(self, n, prerequisites):
        # Step 1: Create adjacency list
        adj = [[] for _ in range(n)]
        
        # Step 2: Create indegree array initialized with 0
        indegree = [0] * n
        
        # Step 3: Build graph and fill indegree array
        for x, y in prerequisites:
            adj[y].append(x)      # Edge from y → x
            indegree[x] += 1      # Increment indegree of x
        
        # Step 4: Initialize queue with all courses having indegree 0
        q = deque([i for i in range(n) if indegree[i] == 0])
        
        # Step 5: List to store topological order
        topo_order = []
        
        # Step 6: Process queue until empty
        while q:
            node = q.popleft()
            topo_order.append(node)
            
            # Step 7: For each neighbor, reduce its indegree
            for nei in adj[node]:
                indegree[nei] -= 1
                
                # Step 8: If indegree becomes 0, add to queue
                if indegree[nei] == 0:
                    q.append(nei)
        
        # Step 9: If all courses are processed, return the order
        if len(topo_order) == n:
            return topo_order
        else:
            # Step 10: Cycle detected → return empty list
            return []
