"""
Six degrees of separation is the theory that everyone and everything is six or fewer steps away, by way of introduction, from any other person in the
world, so that a chain of "a friend of a friend" statements can be made to connect any two people in a maximum of six steps.

Given a friendship relations, find the degrees of two people, return -1 if they can not been connected by friends of friends.

Example
Gien a graph:

1------2-----4
 \          /
  \        /
   \--3--/
{1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4 return 2

Gien a graph:

1      2-----4
             /
           /
          3
{1#2,4#3,4#4,2,3} and s = 1, t = 4 return -1
"""

from collections import deque


# Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """

    def sixDegrees(self, graph, s, t):
        # write your code here
        if graph is None or len(graph) == 0:
            return -1

        queue = deque([s])
        visited = {s, }
        steps = 0
        while queue:
            len_q = len(queue)
            for _ in range(len_q):
                node = queue.popleft()
                if node == t:
                    return steps

                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            steps += 1

        return -1