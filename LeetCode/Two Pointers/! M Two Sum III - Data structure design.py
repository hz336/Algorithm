"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:

add(3); add(1); add(2);
find(3) -> true
find(6) -> false
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}

    def add(self, number: 'int') -> 'None':
        """
        Add the number to an internal data structure..
        """
        if number in self.m:
            self.m[number] = self.m[number] + 1
        else:
            self.m[number] = 1

    def find(self, value: 'int') -> 'bool':
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for k, v in self.m.items():
            if value - k in self.m:
                if value - k != k:
                    return True

                if value - k == k and self.m[k] > 1:
                    return True

        return False

