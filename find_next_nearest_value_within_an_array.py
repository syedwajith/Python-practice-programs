def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            pos += 1
            if pos < len(arr):
                return arr[pos]
            else:
                return None
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return None

def nearest_value(arr):
    arr1 = arr.copy()
    sorted_arr = selection_sort(arr)
    for i in range(len(arr)):
        search_value = interpolation_search(sorted_arr, arr1[i])
        print(f"{arr1[i]}->{search_value}", end = " ")

if __name__ == "__main__":
    arr = list(map(int, input("Enter the values between one space : ").strip().split()))
    res = nearest_value(arr)