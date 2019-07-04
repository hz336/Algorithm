"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least
recently used item before inserting a new item.
"""


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class ListedNode:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.mapping = {}
        self.capacity = capacity
        self.head, self.tail = ListedNode(), ListedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        # Remove current
        curr = self.mapping[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        # Move to tail
        self.move_to_tail(curr)

        return self.mapping[key].val

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.mapping[key].val = value
            return

        if len(self.mapping) == self.capacity:
            self.mapping.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

        curr = ListedNode(key, value)
        self.mapping[key] = curr
        self.move_to_tail(curr)

    def move_to_tail(self, curr):
        curr.prev = self.tail.prev
        self.tail.prev = curr
        curr.prev.next = curr
        curr.next = self.tail



