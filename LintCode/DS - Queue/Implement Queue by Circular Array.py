"""
Implement queue by circulant array. You need to support the following methods:
1. CircularQueue(n): initialize a circular array with size n to store elements
2. boolean isFull(): return true if the array is full
3. boolean isEmpty(): return true if there is no element in the array
4. void enqueue(element): add an element to the queue
5. int dequeue(): pop an element from the queue

Notice
it's guaranteed in the test cases we won't call enqueue if it's full and we also won't call dequeue if it's empty. So it's ok to raise exception in
scenarios described above.

Example
CircularQueue(5)
isFull()   => false
isEmpty() => true
enqueue(1)
dequeue()  => 1
"""


class CircularQueue:
    def __init__(self, n):
        # do intialization if necessary
        self.queue = [None] * n
        self.front = self.rear = self.size = 0

    """
    @return:  return true if the array is full
    """

    def isFull(self):
        # write your code here
        return self.size == len(self.queue)

    """
    @return: return true if there is no element in the array
    """

    def isEmpty(self):
        # write your code here
        return self.size == 0

    """
    @param element: the element given to be added
    @return: nothing
    """

    def enqueue(self, element):
        # write your code here
        self.rear = (self.front + self.size) % len(self.queue)
        self.queue[self.rear] = element
        self.size += 1

    """
    @return: pop an element from the queue
    """

    def dequeue(self):
        # write your code here
        element = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        self.size -= 1

        return element
