def selection_sort(arr, n):
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

def nearest_value(n, arr, m):
    sort_arr = selection_sort(arr, n)
    min_val = 0
    max_val = 0

    for i in range(n):
        if m >= sort_arr[i]:
            min_val = sort_arr[i]
        else:
            if m <= sort_arr[i]:
                max_val = sort_arr[i]
                break

    a = m - min_val
    b = max_val - m

    if a <= b:
        return min_val
    else:
        return max_val
    
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [arr[i] for i in range(n)]
    m = int(input())
    res = nearest_value(n, arr, m)
    print(res)