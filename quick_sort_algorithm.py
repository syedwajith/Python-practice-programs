def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    pivot = arr[n // 2]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)

unsorted_arr = list(map(int, input("Enter the numbers & each no have between one space : ").split()))
sorted_arr = quick_sort(unsorted_arr)
print(sorted_arr)