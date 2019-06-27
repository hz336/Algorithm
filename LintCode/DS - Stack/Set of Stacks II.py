"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the
previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and
should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack). SetOfStacks.popAt(int index) which performs a pop
operation on a specific sub-stack.If we pop an element from stack 1, we need to remove the bottom of stack 2 and push it onto stack 1. We then need
to rollover from stack 3 to stack 2, stack 4 to stack 3, etc.

Example
SetOfStacks(2);  // create a SetOfStacks object with capacity = 2
push(1)
push(2)
push(4)
push(8)
push(16)
popAt(0) // return 2
popAt(0) // return 4
pop()    // return 16

"""

""" Difficulty: Hard """


class SetOfStacks2:
    """
    @param: capacity: an inetger, capacity of sub stack
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.stack = []
        self.capacity = capacity

    """
    @param: v: An integer
    @return: nothing
    """

    def push(self, v):
        # write your code here
        if len(self.stack) == 0:
            self.stack.append([])

        if len(self.stack[-1]) == self.capacity:
            self.stack.append([])

        self.stack[-1].append(v)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        value = self.stack[-1].pop()
        if len(self.stack[-1]) == 0:
            self.stack.pop()

        return value

    """
    @param: index: The index of a specific sub-stack
    @return: top element of the specific sub-stack
    """

    def popAt(self, index):
        # Write your code here
        return self.left_shift(index, True)

    def left_shift(self, index, removeTop):
        if removeTop:
            removed_item = self.stack[index][-1]
            self.stack[index].pop()
        else:
            removed_item = self.stack[index][0]
            self.stack[index].pop(0)

        if len(self.stack[index]) is 0:
            self.stack.pop(index)
        elif len(self.stack) > index + 1:
            v = self.left_shift(index + 1, False)
            self.stack[index].append(v)

        return removed_item

