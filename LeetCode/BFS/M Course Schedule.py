"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""

# Topological Sorting

from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Count each's node indegree (number of edge into node)
        indegree = defaultdict(int)
        edges = defaultdict(list)
        for u, v in prerequisites:
            indegree[u] += 1
            edges[v].append(u)

        # get those nodes with indegree 0 (which are the nodes in graph but not in indegree)
        start_nodes = set()
        for i in range(numCourses):
            if i not in indegree:
                start_nodes.add(i)

        # BFS (from indegree 0, 1, 2..)
        queue = deque(start_nodes)
        visited = start_nodes
        while queue:
            node = queue.popleft()
            for edge in edges[node]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    visited.add(edge)
                    queue.append(edge)

        return len(visited) == numCourses
