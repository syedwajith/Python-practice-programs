def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

unsorted_arr = list(map(int, input("Enter the numbers & each no have between one space : ").split()))
sorted_arr = selection_sort(unsorted_arr)
print(sorted_arr)