"""
Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted
in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.
"""


class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        # Algorithm:
        # 1. Find the first index that A[index] >= target
        # 2. Set two pointers left = index - 1 and right = index
        # 3. Compare A[left] and A[right] to decide which pointer should move

        index = self.helper(A, target, k)
        left, right = index - 1, index
        results = []
        for i in range(k):
            if left < 0:
                results.append(A[right])
                right += 1
            elif right == len(A):
                results.append(A[left])
                left -= 1
            else:
                if target - A[left] <= A[right] - target:
                    results.append(A[left])
                    left -= 1
                else:
                    results.append(A[right])
                    right += 1

        return results

    def helper(self, A, target, k):
        # write your code here
        if A is None or len(A) == 0:
            return []

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] >= target:
            return start

        if A[end] >= target:
            return end

        return len(A)


A = [1, 4, 6, 8]
target = 3
k = 3

sol = Solution()
ans = sol.kClosestNumbers(A, target, k)
print(ans)


