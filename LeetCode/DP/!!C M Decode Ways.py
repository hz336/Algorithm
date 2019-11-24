"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

""" 
计数型DP
Time Complexity: O(N)
Space Complexity: O(N)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        f = [0] * (len(s) + 1)
        f[0] = 1

        for i in range(1, len(s) + 1):
            if int(s[i - 1]) != 0:
                f[i] += f[i - 1]

            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26:
                f[i] += f[i - 2]

        return f[-1]


"""
Follow Up: Could you print all the combinations of the message? 
DFS
"""
class Solution:
    def __init__(self):
        pass

    def decodings(self, s):
        if s is None or len(s) == 0:
            return []

        subset = []
        results = []
        self.dfs(s, 0, subset, results)
        return results

    def dfs(self, s, index, subset, results):
        if index == len(s):
            results.append(subset)
            return

        if 1 <= int(s[index]) <= 9:
            word = chr(int(s[index]) - 1 + ord('A'))
            self.dfs(s, index + 1, subset + [word], results)

        if index + 1 < len(s) and 10 <= int(s[index: index + 2]) <= 26:
            word = chr(int(s[index: index + 2]) - 1 + ord('A'))
            self.dfs(s, index + 2, subset + [word], results)


test = Solution()
test_res = test.decodings("123")
print(test_res)