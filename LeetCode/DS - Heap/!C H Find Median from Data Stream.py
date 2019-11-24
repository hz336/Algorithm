"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of
the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""

"""
The invariant of the algorithm is two heaps, small and large, each represent half of the current list. The length of smaller half is kept to be n / 2 
at all time and the length of the larger half is either n / 2 or n / 2 + 1 depend on n's parity.

Note that the heapq in python is a min heap, thus we need to invert the values in the smaller half to mimic a "max heap".
"""

