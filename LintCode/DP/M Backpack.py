"""
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

Example
If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10.
If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.

Challenge
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.
"""

"""
Time Complexity: O(mn)
Space complexity: O(m)
"""
class Solution:
    def backPack(self, m, A):
        if A is None or len(A) == 0:
            return False

        n = len(A)
        f = [False for _ in range(m + 1)]
        f[0] = True

        for item in range(1, n + 1):
            for weight in range(m, 0, -1):
                if weight >= A[item - 1] and f[weight - A[item - 1]]:
                    f[weight] = True

        for weight in range(m, -1, -1):
            if f[weight] is True:
                return weight


target = 7
nums = [2,3,6,7]
sol = Solution()
ans = sol.backPack(target, nums)

"""
Time Complexity: O(mn)
Space complexity: O(2m)
"""
class Solution_v2:
    def backPack(self, m, A):
        if A is None or len(A) == 0:
            return False

        n = len(A)
        f = [[False for _ in range(m + 1)] for _ in range(2)]
        old, now = 0, 1
        f[now][0] = True

        for item in range(1, n + 1):
            old, now = now, old
            for weight in range(m + 1):
                f[now][weight] = f[old][weight]
                if weight >= A[item - 1] and f[old][weight - A[item - 1]]:
                    f[now][weight] = True

        for weight in range(m, -1, -1):
            if f[now][weight] is True:
                return weight


"""
Time Complexity: O(mn)
Space complexity: O(mn)
"""
class Solution_v3:
    def backPack(self, m, A):
        if A is None or len(A) == 0:
            return False

        n = len(A)
        f = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        f[0][0] = True

        for item in range(1, n + 1):
            for weight in range(m + 1):
                f[item][weight] = f[item - 1][weight]
                if weight >= A[item - 1] and f[item - 1][weight - A[item - 1]]:
                    f[item][weight] = True

        for weight in range(m, -1, -1):
            if f[n][weight] is True:
                return weight
