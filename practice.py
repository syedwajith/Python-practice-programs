def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if min_index > j:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

a = {1:2, 2:2, 5:1, 3:1}
print(selection_sort(a))