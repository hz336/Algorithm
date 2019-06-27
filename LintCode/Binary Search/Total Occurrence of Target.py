"""
Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.
"""


class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def totalOccurrence(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return 0

        # Find the first position
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                end = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[start] == target:
            head = start
        elif A[end] == target:
            head = end
        else:
            return 0

        # Find the last position
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[end] == target:
            tail = end
        elif A[start] == target:
            tail = start
        else:
            return 0

        return tail - head + 1


sol = Solution()
ans = sol.totalOccurrence(A=[1, 3, 3, 4, 5], target=3)
print(ans)




