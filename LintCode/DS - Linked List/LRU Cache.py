"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least
recently used item before inserting a new item.
"""


class LinkedNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.mapping = {}
        self.capacity = capacity
        self.head, self.tail = LinkedNode(), LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key not in self.mapping:
            return -1

        # Remove current
        current = self.mapping[key]
        current.prev.next = current.next
        current.next.prev = current.prev

        # Move current to tail
        self.move_to_tail(current)

        return self.mapping[key].val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        # self.get() function will move key to the end of the cache
        if self.get(key) != -1:
            self.mapping[key].val = value
            return

        if len(self.mapping) == self.capacity:
            self.mapping.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

        node = LinkedNode(key, value)
        self.mapping[key] = node
        self.move_to_tail(node)

    def move_to_tail(self, current):
        current.prev = self.tail.prev
        self.tail.prev = current
        current.prev.next = current
        current.next = self.tail

