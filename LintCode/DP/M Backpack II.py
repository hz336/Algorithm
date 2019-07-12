"""
Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?

Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.

Challenge
O(n x m) memory is acceptable, can you do it in O(m) memory?
"""


"""
Time Complexity: O(mn)
Space complexity: O(m)
"""
class Solution:
    def backPackII(self, m, A, V):
        if A is None or V is None or len(A) == 0 or len(V) == 0:
            return 0

        n = len(A)
        f = [float('-inf') for _ in range(m + 1)]
        f[0] = 0

        for i in range(1, n + 1):
            for j in range(m, -1, -1):
                if j >= A[i - 1] and f[j - A[i - 1]] != float('-inf'):
                    f[j] = max(f[j], f[j - A[i - 1]] + V[i - 1])

        return max(f)


"""
Time Complexity: O(mn)
Space complexity: O(2n)
"""
class Solution:
    def backPackII(self, m, A, V):
        if A is None or V is None or len(A) == 0 or len(V) == 0:
            return 0

        n = len(A)
        f = [[float('-inf') for _ in range(m + 1)] for _ in range(2)]
        old, now = 0, 1
        f[old][0] = f[now][0] = 0

        for i in range(1, n + 1):
            old, now = now, old
            for j in range(m + 1):
                f[now][j] = f[old][j]
                if j >= A[i - 1] and f[old][j - A[i - 1]] != float('-inf'):
                    f[now][j] = max(f[old][j], f[old][j - A[i - 1]] + V[i - 1])

        return max(f[now][:])


"""
Time Complexity: O(mn)
Space complexity: O(mn)
"""
class Solution:
    def backPackII(self, m, A, V):
        if A is None or V is None or len(A) == 0 or len(V) == 0:
            return 0

        n = len(A)
        f = [[float('-inf') for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][0] = 0

        for i in range(1, n + 1):
            for j in range(m + 1):
                f[i][j] = f[i - 1][j]
                if j >= A[i - 1] and f[i - 1][j - A[i - 1]] != float('-inf'):
                    f[i][j] = max(f[i - 1][j], f[i - 1][j - A[i - 1]] + V[i - 1])

        return max(f[n][:])


"""
Time Complexity: O(mn)
Space complexity: O(mn)
Print Optimal Path 
"""
import math


class Solution_v3:
    def backPackII(self, m, A, V):
        if A is None or V is None:
            return 0

        n = len(A)
        f = [[-math.inf for _ in range(m + 1)] for _ in range(n + 1)]
        pi = [[-math.inf for _ in range(m + 1)] for _ in range(n + 1)]
        for item in range(n + 1):
            f[item][0] = 0

        for item in range(1, n + 1):
            for weight in range(1, m + 1):
                f[item][weight] = f[item - 1][weight]
                pi[item][weight] = 0
                if weight >= A[item - 1] and f[item - 1][weight - A[item - 1]] != -math.inf:
                    f[item][weight] = max(f[item][weight], f[item - 1][weight - A[item - 1]] + V[item - 1])
                    pi[item][weight] = 1

        result = -math.inf
        last_weight = None
        for weight in range(1, m + 1):
            result = max(result, f[n][weight])
            if result == f[n][weight]:
                last_weight = weight

        for item in range(n, 0, -1):
            if pi[item][last_weight] == 1:
                print("weight " + str(A[item - 1]) + "kg, Value $" + str(V[item - 1]))
                last_weight -= A[item - 1]

        return max(f[n][:])


m = 10
A = [2, 3, 5, 7]
V = [1, 5, 2, 4]
sol = Solution_v3()
ans = sol.backPackII(m, A, V)
print(ans)


