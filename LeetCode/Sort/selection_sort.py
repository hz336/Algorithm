def selection_sort(lst):
    for i in range(len(lst)):
        mn = i
        for j in range(i, len(lst)):
            if lst[j] < lst[mn]:
                mn = j
        lst[i], lst[mn] = lst[mn], lst[i]

        print(lst)

    return lst


input = [5, 4, 3, 2, 1]
print(input)
output = selection_sort(input)
print(output)