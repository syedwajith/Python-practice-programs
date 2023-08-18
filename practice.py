def selection_sort(arr):
    n = len(arr)
    for i in arr.keys():
        min_key = i
        for j in arr.keys():
            if min_key > j:
                min_key = j
        arr[i], arr[min_key] = arr[min_key], arr[i]

    return arr

a = {1:2, 2:2, 5:1, 3:1}
print(selection_sort(a))