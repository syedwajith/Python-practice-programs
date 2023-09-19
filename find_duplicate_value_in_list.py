def d(arr):
    dup = []
    u = []
    for i in range(len(arr)):
        if arr[i] not in u:
            u.append(arr[i])
        elif arr[i] in u:
            dup.append(arr[i])

    return dup

arr = list(map(int, input().split()))
res = d(arr)
print(res)