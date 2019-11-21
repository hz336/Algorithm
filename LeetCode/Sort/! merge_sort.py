"""
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

def merge_sort(lst):
    temp = [0] * len(lst)
    merge_sort_helper(lst, temp, 0, len(lst) - 1)
    return lst


def merge_sort_helper(lst, temp, start, end):
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort_helper(lst, temp, start, mid)
    merge_sort_helper(lst, temp, mid + 1, end)
    merge(lst, temp, start, mid, end)


def merge(lst, temp, start, mid, end):
    left, right = start, mid + 1
    index = start
    while left <= mid and right <= end:
        if lst[left] < lst[right]:
            temp[index] = lst[left]
            left += 1
        else:
            temp[index] = lst[right]
            right += 1

        index += 1

    while left <= mid:
        temp[index] = lst[left]
        left += 1
        index += 1

    while right <= end:
        temp[index] = lst[right]
        right += 1
        index += 1

    for index in range(start, end + 1):
        lst[index] = temp[index]


input = [8, 7, 6, 5, 4, 3, 2, 1]
print(input)
output = merge_sort(input)
print(output)




