def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print(lst)

    return lst


input = [5, 4, 3, 2, 1]
print(input)
output = bubble_sort(input)
print(output)

