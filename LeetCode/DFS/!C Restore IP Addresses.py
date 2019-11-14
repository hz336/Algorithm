"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

"""
Time Complexity: O(3 x 3 x 3) = O(27)
Space Complexity: constant space
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        self.dfs(s, 4, [], results)
        return ['.'.join(x) for x in results]

    def dfs(self, s, k, temp, results):
        if len(s) > k * 3:
            return

        if k == 0:
            results.append(temp)
            return

        for i in range(min(3, len(s) - k + 1)):
            # if not singal digit and starts with 0, continue
            if i > 0 and s[0] == '0':
                continue

            # if three digits and larger than 255, continue
            if i == 2 and int(s[:3]) > 255:
                continue

            self.dfs(s[i + 1:], k - 1, temp + [s[:i + 1]], results)

