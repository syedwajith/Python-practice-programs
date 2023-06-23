def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return None

my_arr = list(map(int, input("Enter the value & each value have one single space :").split()))
target_value = int(input("Enter the target value :"))
result = linear_search(my_arr, target_value)
print(f"The target value is founded at index : {result}")