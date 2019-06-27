"""
Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.

Notice
If the element in the given list is a list, it can contain list too.

Example
Given [1,2,[1,2]], return [1,2,1,2].
Given [4,[3,[2,[1]]]], return [4,3,2,1].
"""


class Solution(object):
    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        if isinstance(nestedList, int):
            return [nestedList]

        results = []
        for e in nestedList:
            results.extend(self.flatten(e))

        return results
