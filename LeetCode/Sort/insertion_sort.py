def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i
        temp = lst[j]
        while j > 0 and temp < lst[j - 1]:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = temp

        print(lst)

    return lst


input = [5, 4, 3, 2, 1]
print(input)
output = insertion_sort(input)
print(output)
