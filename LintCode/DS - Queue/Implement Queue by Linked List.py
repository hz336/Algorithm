"""
Implement a Queue by linked list. Support the following basic methods:

enqueue(item). Put a new item in the queue.
dequeue(). Move the first item out of the queue, return it.

Example
enqueue(1)
enqueue(2)
enqueue(3)
dequeue() // return 1
enqueue(4)
dequeue() // return 2
"""


class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """

    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, item):
        # write your code here
        node = ListNode(item)

        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    """
    @return: An integer
    """

    def dequeue(self):
        # write your code here
        if self.head:
            value = self.head.val
            self.head = self.head.next

            if self.head is None:
                self.head = self.tail = None

            return value
