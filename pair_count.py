def pair_counting(ar):
    arr = []
    pair_count = 0
    for i in ar:
        if i in arr:
            arr.remove(i)
            pair_count += 1
        else:
            arr.append(i)
            
    return pair_count

n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
ar = [ar[i] for i in range(n)]
result = pair_counting(ar)
print(result)