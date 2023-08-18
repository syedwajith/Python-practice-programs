def rev_arr(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr

arr = list(map(int, input().split()))
res = rev_arr(arr)
print(res)