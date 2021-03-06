"""
Average Time Complexity: O(nlogn)
Worst Time Complexity: O(n^2)
Space Complexity: O(1)
"""


def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)
    return lst


def quick_sort_helper(lst, start, end):
    if start >= end:
        return

    left, right = start, end

    # Point 1: get value, not index.
    # The value at a fixed index might be changing.
    pivot = lst[(start + end) // 2]

    # Point 2: left <= right, not <
    while left <= right:
        # Point 3: lst[left] < pivot, not <=
        while left <= right and lst[left] < pivot:
            left += 1

        while left <= right and lst[right] > pivot:
            right -= 1

        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

        print(lst)

    quick_sort_helper(lst, start, right)
    quick_sort_helper(lst, left, end)


input = [2, 1, 6, 5, 4, 3, 8, 7]
print(input)
output = quick_sort(input)
print(output)






















