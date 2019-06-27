"""
Given n unique integers, number k (1<=k<=n) and target.
Find all possible k integers where their sum is target.

Example
Given [1,2,3,4], k = 2, target = 5. Return:

[
  [1,4],
  [2,3]
]
"""


class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        # write your code here
        A.sort()
        results = []
        self.dfs(A, k, target, 0, [], results)

        return results

    def dfs(self, A, k, target, index, subset, results):
        if target == 0 and len(subset) == k:
            results.append(subset.copy())
            return

        for i in range(index, len(A)):
            if target - A[i] < 0 or len(subset) >= k:
                break

            subset.append(A[i])
            self.dfs(A, k, target - A[i], i + 1, subset, results)
            subset.pop()


