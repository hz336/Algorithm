"""
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

add(1); add(3); add(5);
find(4) // return true
find(7) // return false
"""


class TwoSum:
    def __init__(self):
        self.dic = {}

    """
    @param: number: An integer
    @return: nothing
    """
    def add(self, number):
        if number in self.dic:
            self.dic[number] += 1
        else:
            self.dic[number] = 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        for k, v in self.dic.items():
            if value - k in self.dic and (value - k != k or v > 1):
                return True

        return False






