"""
Merge two given sorted integer array A and B into a new sorted integer array.
"""


class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        index_A = 0
        index_B = 0
        results = []

        while index_A < len(A) and index_B < len(B):
            if A[index_A] <= B[index_B]:
                results.append(A[index_A])
                index_A += 1
            else:
                results.append(B[index_B])
                index_B += 1

        while index_A < len(A):
            results.append(A[index_A])
            index_A += 1

        while index_B < len(B):
            results.append(B[index_B])
            index_B += 1

        return results
