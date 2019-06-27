"""
On a 3x3 board, there are 8 tiles represented by the integers 1 through 8, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

Given an initial state of the puzzle board and final state, return the least number of moves required so that the initial state to final state.

If it is impossible to move from initial state to final state, return -1.

Example
Given an initial state:

[
 [2,8,3],
 [1,0,4],
 [7,6,5]
]
and a final state:

[
 [1,2,3],
 [8,0,4],
 [7,6,5]
]
Return 4
Explanation:

[                 [
 [2,8,3],          [2,0,3],
 [1,0,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [2,0,3],          [0,2,3],
 [1,8,4],   -->    [1,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [0,2,3],          [1,2,3],
 [1,8,4],   -->    [0,8,4],
 [7,6,5]           [7,6,5]
]                 ]

[                 [
 [1,2,3],          [1,2,3],
 [0,8,4],   -->    [8,0,4],
 [7,6,5]           [7,6,5]
]                 ]
"""

from collections import deque


class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """

    def minMoveStep(self, init_state, final_state):
        # write your code here
        init_str = self.list_to_string(init_state)
        final_str = self.list_to_string(final_state)

        x_delta = [-1, 1, 0, 0]
        y_delta = [0, 0, -1, 1]

        queue = deque([init_str])
        visited = {init_str, }
        steps = 0
        while queue:
            len_q = len(queue)
            for _ in range(len_q):
                state = queue.popleft()
                if state == final_str:
                    return steps

                found = state.find('0')

                x, y = found // 3, found % 3

                for i in range(4):
                    new_x = x + x_delta[i]
                    new_y = y + y_delta[i]

                    if self.check(new_x, new_y):
                        index = new_x * 3 + new_y
                        new_state = list(state)
                        new_state[found], new_state[index] = new_state[index], new_state[found]
                        new_state = self.list_to_string(new_state)

                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append(new_state)

            steps += 1

        return -1

    def list_to_string(self, state):
        return ''.join(str(c) for part in state for c in part)

    def check(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3




