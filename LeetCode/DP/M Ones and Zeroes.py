"""
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.


Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
"""

"""
Quesiton is a little bit ambiguous, so can be ignored.
Time Complexity: O(kmn)
Space Complexity: O(kmn)
"""
class Solution_v1:
    def findMaxForm(self, strs, m, n):
        if strs is None or len(strs) == 0:
            return 0

        k = len(strs)
        cnt0 = [0] * k
        cnt1 = [0] * k
        for i in range(k):
            for c in strs[i]:
                if c == '0':
                    cnt0[i] += 1
                else:
                    cnt1[i] += 1

        f = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(k + 1)]

        for s in range(k + 1):
            for i in range(m + 1):
                for j in range(n + 1):
                    if s == 0:
                        continue

                    f[s][i][j] = f[s - 1][i][j]
                    if i >= cnt0[s - 1] and j >= cnt1[s - 1]:
                        f[s][i][j] = max(f[s][i][j], f[s - 1][i - cnt0[s - 1]][j - cnt1[s - 1]] + 1)

        return f[k][m][n]

"""
Time Complexity: O(kmn)
Space Complexity: O(2mn)
"""
class Solution_v2:
    def findMaxForm(self, strs, m, n):
        if strs is None or len(strs) == 0:
            return 0

        k = len(strs)
        cnt0 = [0] * k
        cnt1 = [0] * k
        for i in range(k):
            for c in strs[i]:
                if c == '0':
                    cnt0[i] += 1
                else:
                    cnt1[i] += 1

        f = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(2)]
        old, now = 0, 1

        for s in range(k + 1):
            old, now = now, old
            for i in range(m + 1):
                for j in range(n + 1):
                    if s == 0:
                        continue

                    f[now][i][j] = f[old][i][j]
                    if i >= cnt0[s - 1] and j >= cnt1[s - 1]:
                        f[now][i][j] = max(f[now][i][j], f[old][i - cnt0[s - 1]][j - cnt1[s - 1]] + 1)

        return f[now][m][n]


"""
Time Complexity: O(kmn)
Space Complexity: O(2mn)
"""
class Solution_v3:
    def findMaxForm(self, strs, m, n):
        if strs is None or len(strs) == 0:
            return 0

        k = len(strs)
        f = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(2)]
        old, now = 0, 1

        for s in range(k + 1):
            old, now = now, old

            if s > 0:
                cnt0, cnt1 = 0, 0
                for c in strs[s - 1]:
                    if c == '0':
                        cnt0 += 1
                    else:
                        cnt1 += 1

            for i in range(m + 1):
                for j in range(n + 1):
                    if s == 0:
                        continue

                    f[now][i][j] = f[old][i][j]
                    if i >= cnt0 and j >= cnt1:
                        f[now][i][j] = max(f[now][i][j], f[old][i - cnt0][j - cnt1] + 1)

        return f[now][m][n]
