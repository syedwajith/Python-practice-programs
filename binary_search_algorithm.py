def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high :
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1  # It search from left to right
        else:
            high = mid - 1  # It search from right to left

    return None

my_arr = list(map(int, input("Enter the value orderwise & each value have one single space :").split()))
target_value = int(input("Enter the target value :"))
result = binary_search(my_arr, target_value)
print(f"The target value is founded at index : {result}")