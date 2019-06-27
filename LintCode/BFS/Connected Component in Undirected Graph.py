"""
Find the number connected component in the undirected graph. Each node in the graph contains a label and a list of its neighbors. (a connected
component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is
connected to no additional vertices in the supergraph.)

Notice
Each connected component should sort by label.

Example
Given graph:

A------B  C
 \     |  |
  \    |  |
   \   |  |
    \  |  |
      D   E
Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}
"""

from collections import deque


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """

    def connectedSet(self, nodes):
        # write your code here
        if nodes is None or len(nodes) == 0:
            return []

        visited = {}
        for node in nodes:
            visited[node] = False

        results = []
        for node in nodes:
            if not visited[node]:
                visited[node] = True
                self.bfs(node, visited, results)

        return results

    def bfs(self, node, visited, results):
        comp = []
        queue = deque([node])
        while queue:
            node = queue.popleft()
            comp.append(node.label)
            for neighbor in node.neighbors:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        comp.sort()
        results.append(comp)




