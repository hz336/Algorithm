"""
Given an an unsorted array, sort the given array. You are allowed to do only following operation on array.

flip(arr, i): Reverse array from 0 to i
Unlike a traditional sorting algorithm, which attempts to sort with the fewest comparisons possible, the goal is to sort the sequence in as few reversals as possible.

Notice
You only call flip function.
Don't allow to use any sort function or other sort methods.

Example
Given array = [6, 7, 10, 11, 12, 20, 23]
Use flip(arr, i) function to sort the array.
"""

"""
class FlipTool:

    @classmethod
    def flip(cls, arr, i):
        ...
"""


class Solution:
    """
    @param array: an integer array
    @return: nothing
    """

    def pancakeSort(self, array):
        # Write your code here
        for i in range(len(array) - 1, -1, -1):
            num_max = -math.inf
            idx_max = None
            for j in range(i + 1):
                if array[j] > num_max:
                    num_max = array[j]
                    idx_max = j

            FlipTool.flip(array, idx_max)
            FlipTool.flip(array, i)


