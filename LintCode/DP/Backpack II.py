"""
Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?

Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.

Challenge
O(n x m) memory is acceptable, can you do it in O(m) memory?
"""

import math


"""
Time Complexity: O(mn)
Space complexity: O(m)
"""
class Solution_v1:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
        if A is None or V is None:
            return 0

        n = len(A)
        f = [-math.inf] * (m + 1)
        f[0] = 0

        for item in range(1, n + 1):
            for weight in range(m, -1, -1):
                if weight >= A[item - 1] and f[weight - A[item - 1]] != -math.inf:
                    f[weight] = max(f[weight], f[weight - A[item - 1]] + V[item - 1])

        return max(f)


"""
Time Complexity: O(mn)
Space complexity: O(mn)
"""
class Solution_v2:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
        if A is None or V is None:
            return 0

        n = len(A)
        f = [[-math.inf for _ in range(m + 1)] for _ in range(n + 1)]
        for item in range(n + 1):
            f[item][0] = 0

        for item in range(1, n + 1):
            for weight in range(1, m + 1):
                f[item][weight] = f[item - 1][weight]
                if weight >= A[item - 1] and f[item - 1][weight - A[item - 1]] != -math.inf:
                    f[item][weight] = max(f[item][weight], f[item - 1][weight - A[item - 1]] + V[item - 1])

        print(f)

        return max(f[n][:])

"""
Time Complexity: O(mn)
Space complexity: O(mn)
Optimal Path 
"""
class Solution_v3:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
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


