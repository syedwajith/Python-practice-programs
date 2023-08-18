def sub_arr(arr):
    frame = 1
    max_sum_val = 0
    current_sum = 0
    max_sum_count = 0
    current_count = 0
    while frame <= len(arr):
        for i in range(len(arr)):
            for j in range(i,i+frame):
                if j < len(arr):
                    current_sum += arr[j]
                    current_count += 1
                
            if max_sum_val < current_sum:
                max_sum_val = current_sum
                max_sum_count = current_count

            current_sum = 0
            current_count = 0
            
        frame += 1
    
    return max_sum_val, max_sum_count

arr = list(map(int, input().split()))
res = sub_arr(arr)
print(res)