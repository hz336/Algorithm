"""
Given n processes, each process has a unique PID (process id) and its PPID (parent process id).

Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. Only one process has PPID
that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.

We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the
corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. You
should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

Notice
The given kill id is guaranteed to be one of the given PIDs.
n >= 1.

Example
Given pid = [1, 3, 10, 5], ppid = [3, 0, 5, 3], kill = 5, return [5,10].

Explanation:
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
"""

from collections import deque, defaultdict


class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """

    def killProcess(self, pid, ppid, kill):
        # Write your code here
        mapping = defaultdict(set)
        for child, parent in zip(pid, ppid):
            mapping[parent].add(child)

        queue = deque([kill])
        results = []
        while queue:
            parent = queue.popleft()
            results.append(parent)
            for child in mapping[parent]:
                queue.append(child)

        return results