"""
Sort a stack in ascending order (with biggest terms on top).

You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure (e.g. array).

You don't need to return a new stack, just sort elements in the given parameter stack.

In python, you can use list as stack
stack = [1,2,3,4]
Get top element: stack[-1]  -> 4
Pop element: stack.pop()   -> 4
Push element: stack.append(5)
check the size of stack: len(stack)
"""


class Solution:
    """
    @param: stack: an integer stack
    @return: void
    """

    def stackSorting(self, stack):
        # write your code here
        temp = []
        while len(stack):
            if not len(temp) or temp[-1] >= stack[-1]:
                temp.append(stack.pop())
            else:
                value = stack.pop()
                while len(temp) and temp[-1] <= value:
                    stack.append(temp.pop())
                stack.append(value)

                while len(temp):
                    stack.append(temp.pop())

        while len(temp):
            stack.append(temp.pop())

