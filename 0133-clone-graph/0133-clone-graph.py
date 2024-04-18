"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        
        print("Visited", visited)
        print("before dfs")

        def dfs(original):
            if original in visited:
                # print("original", original.val)
                # print("visited[original]", visited[original].val)
                return visited[original]
            
            clone = Node(original.val)
            # print("clone", clone.val)
            visited[original] = clone
            # print("visited[original]", (visited[original]).val)

            # print("original.neighbors", original.neighbors)
            for neighbor in original.neighbors:
                # print("neighbor", neighbor.val)
                # print("CALLING ######################################")
                clone.neighbors.append(dfs(neighbor))
                # print("clone.neighbors.val", clone.neighbors)
            
            return clone
        return dfs(node)   