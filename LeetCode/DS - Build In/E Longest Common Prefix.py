"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

"""
Greedy Algorithm
Time Complexity: O(number of all characters in the whole list)
Space Complexity: O(1)
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ""

        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]

        return shortest



