"""
Giving a string with number from 1-n in random order, but miss 1 number.Find that number.

Example
Given n = 20, str = 19201234567891011121314151618

return 17
"""


class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, string):
        # write your code here
        visited = [False for _ in range(n + 1)]

        target = self.dfs(n, string, 0, visited)

        return target

    def dfs(self, n, string, index, visited):
        if index == len(string):
            result = []
            for i in range(1, n + 1):
                if not visited[i]:
                    result.append(i)

            if len(result) == 1:
                return result[0]
            else:
                return -1

        for step in range(1, 3):
            if string[index] == '0':
                continue

            num = int(string[index: index + step])
            if 1 <= num <= n and not visited[num]:
                visited[num] = True

                target = self.dfs(n, string, index + step, visited)
                if target != -1:
                    return target

                visited[num] = False

        return -1
