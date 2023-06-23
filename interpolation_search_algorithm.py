def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return None

my_arr = list(map(int, input("Enter the value orderwise & each value have one single space :").split()))
target_value = int(input("Enter the target value :"))
result = interpolation_search(my_arr, target_value)
print(f"The target value is founded at index : {result}")