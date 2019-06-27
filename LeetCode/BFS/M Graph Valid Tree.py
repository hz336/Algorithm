"""
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make
up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
"""

"""
Time Complexity: O(number of points + number of edges)
Space Complexity: O(number of points + number of edges)
"""


from collections import deque
from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n <= 0:
            return False

        if len(edges) != n - 1:
            return False

        # Get all neighbors
        neighbors = defaultdict(list)
        for u, v in edges:
            neighbors[v].append(u)
            neighbors[u].append(v)

        # Check connectivity
        queue = deque([0])
        visited = {0, }
        while queue:
            node = queue.popleft()
            for i in neighbors[node]:
                if i in visited:
                    continue
                queue.append(i)
                visited.add(i)

        return len(visited) == n
