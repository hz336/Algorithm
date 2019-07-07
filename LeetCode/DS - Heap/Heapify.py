"""
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].

What is heap?
    Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the
    minimum/maximum element in the heap, "top" return the minimum/maximum element.

What is heapify?
    Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and
    A[i * 2 + 2] >= A[i].

What if there is a lot of solutions?
    Return any of them.

Example
    Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.
"""

class Solution_v1:
    def heapify(self, A):
        for i in range(len(A) // 2, -1, -1):
            self.siftdown(A, i)

    def siftdown(self, A, index):
        while index < len(A):
            smallest = index

            if index * 2 + 1 < len(A) and A[int(index * 2) + 1] < A[smallest]:
                smallest = int(index * 2) + 1

            if index * 2 + 2 < len(A) and A[int(index * 2) + 2] < A[smallest]:
                smallest = int(index * 2) + 2

            if smallest == index:
                break

            A[index], A[smallest] = A[smallest], A[index]
            index = smallest



import heapq


class Solution_v2:
    def heapify(self, A):
        heapq.heapify(A)


