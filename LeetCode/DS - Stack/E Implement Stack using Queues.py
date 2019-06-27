"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
"""

from collections import deque


"""
Time Complexity: push - O(1), pop - O(n)
Space Complexity: O(n)
Method 1 using deque in python
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: 'int') -> 'None':
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> 'int':
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        value = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1

        return value

    def top(self) -> 'int':
        """
        Get the top element.
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        value = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        self.queue1.append(value)

        return value

    def empty(self) -> 'bool':
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0


"""
Time Complexity: push - O(1), pop - O(1)
Space Complexity: O(n)
Method 2 using list in python, only if list is allowed.
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: 'int') -> 'None':
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> 'int':
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop()

    def top(self) -> 'int':
        """
        Get the top element.
        """
        return self.stack[-1]

    def empty(self) -> 'bool':
        """
        Returns whether the stack is empty.
        """
        return len(self.stack) == 0
