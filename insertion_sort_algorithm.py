def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

unsorted_arr = list(map(int, input("Enter the numbers & each no have between one space : ").split()))
sorted_arr = insertion_sort(unsorted_arr)
print(sorted_arr)