"""
Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right.
Indices of the integers in the subsequence should be continuous.

Example
For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """

    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return 0

        count_up = count_down = 1
        num_max_up = num_max_down = 1
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                count_up += 1
                num_max_up = max(num_max_up, count_up)
            else:
                count_up = 1

            if A[i] < A[i - 1]:
                count_down += 1
                num_max_down = max(num_max_down, count_down)
            else:
                count_down = 1

        return max(num_max_up, num_max_down)




