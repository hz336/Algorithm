"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""

"""
Time Complexity: O(5^(n/2))
Space Complexity: O(n/2  + 5^(n/2)), n/2 layers with 5^(n/2) elements.
"""


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.helper(n, n)

    def helper(self, n, n_max):
        if n == 0:
            return [""]

        if n == 1:
            return ["0", "1", "8"]

        center = self.helper(n - 2, n_max)

        results = []
        for i in range(len(center)):
            string = center[i]

            if n != n_max:
                results.append('0' + string + '0')

            results.append('1' + string + '1')
            results.append('6' + string + '9')
            results.append('8' + string + '8')
            results.append('9' + string + '6')

        return results




