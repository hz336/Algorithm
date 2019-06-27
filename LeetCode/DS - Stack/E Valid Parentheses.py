"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def isValid(self, s: 'str') -> 'bool':
        if s is None:
            return False

        if len(s) == 0:
            return True

        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False

                if s[i] == ')' and stack[-1] != '(':
                    return False

                if s[i] == ']' and stack[-1] != '[':
                    return False

                if s[i] == '}' and stack[-1] != '{':
                    return False

                stack.pop()

        return len(stack) == 0

