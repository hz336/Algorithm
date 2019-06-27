"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
"""


# Version 1. Queue
class MovingAverage1:
    def __init__(self, size):
        # do intialization if necessary
        from multiprocessing import Queue
        self.queue = Queue()
        self.size = size
        self.sum = 0.0

    def next(self, val):
        # write your code here
        self.sum += val
        if self.queue.qsize() == self.size:
            self.sum -= self.queue.get()
        self.queue.put(val)

        return self.sum / self.queue.qsize()


# Version 2. List
class MovingAverage2:
    def __init__(self, size):
        # do intialization if necessary
        self.id = 0
        self.size = size
        self.results = [0] * (size + 1)

    def next(self, val):
        # write your code here
        self.id += 1
        self.results[self.mod(self.id)] = self.results[self.mod(self.id - 1)] + val
        if self.id >= self.size:
            return (self.results[self.mod(self.id)] - self.results[self.mod(self.id - self.size)]) / self.size
        else:
            return self.results[self.mod(self.id)] / self.id

    def mod(self, x):
        return x % (self.size + 1)


obj = MovingAverage1(size=3)
print(obj.next(1))
print(obj.next(2))
print(obj.next(3))
print(obj.next(4))