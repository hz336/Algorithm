"""
Implement a Queue by linked list. Provide the following basic methods:

push_front(item). Add a new item to the front of queue.
push_back(item). Add a new item to the back of the queue.
pop_front(). Move the first item out of the queue, return it.
pop_back(). Move the last item out of the queue, return it.
"""


class Node:
    def __init__(self, _val):
        self.next = self.prev = None
        self.val = _val


class Dequeue:
    def __init__(self):
        # do intialization if necessary
        self.first, self.last = None, None

    """
    @param: item: An integer
    @return: nothing
    """

    def push_front(self, item):
        # write your code here
        node = Node(item)
        if self.first is None:
            self.first = self.last = node
        else:
            node.next = self.first
            self.first.prev = node
            self.first = node

    """
    @param: item: An integer
    @return: nothing
    """

    def push_back(self, item):
        # write your code here
        node = Node(item)
        if self.last is None:
            self.first = self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node

    """
    @return: An integer
    """

    def pop_front(self):
        # write your code here
        if self.first is not None:
            item = self.first.val
            self.first = self.first.next

            if self.first is not None:
                self.first.prev = None
            else:
                self.last = None

            return item

    """
    @return: An integer
    """

    def pop_back(self):
        # write your code here
        if self.last is not None:
            item = self.last.val
            self.last = self.last.prev

            if self.last is not None:
                self.last.next = None
            else:
                self.first = None

            return item






