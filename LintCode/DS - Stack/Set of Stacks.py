"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the
previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and
should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single
stack (that is, pop() should return the same values as it would if there were just a single stack).

Example
SetOfStacks(2);  // create a SetOfStacks object with capacity = 2
push(1)
push(2)
push(4)
push(8)
push(16)
pop() // return 16
pop() // return 8
pop() // return 4
"""


class SetOfStacks:
    """
    @param: capacity: An inetger, capacity of sub stack
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.stacks = []
        self.capacity = capacity

    """
    @param: v: An integer
    @return: nothing
    """

    def push(self, v):
        # write your code here
        if len(self.stacks) == 0:
            self.stacks.append([])

        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])

        self.stacks[-1].append(v)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        if len(self.stacks) == 0:
            return None

        value = self.stacks[-1].pop()

        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

        return value





