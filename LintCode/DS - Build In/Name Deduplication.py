"""
Given a list of names, remove the duplicate names. Two name will be treated as the same name if they are equal ignore the case.

Return a list of names without duplication, all names should be in lowercase, and keep the order in the original list.

Example
Given:

["James", "james", "Bill Gates", "bill Gates", "Hello World", "HELLO WORLD", "Helloworld"]
return:

["james", "bill gates", "hello world", "helloworld"]
"""


class Solution:
    """
    @param: : a string array
    @return: a string array
    """

    def nameDeduplication(self, names):
        # write your code here
        results = set()

        for name in names:
            results.add(name.lower())

        return list(results)
