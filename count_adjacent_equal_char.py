def compress_str(s):
    arr = []
    for i in range(0, len(s)):
        count = 0
        for j in range(i,len(s)):
            if s[i] == s[j]:
                count += 1
            else:
                break
        t = (count, s[i])
        if len(arr) == 0:
            arr.append(t)
        elif arr[len(arr)-1][1] != t[1]:
            arr.append(t)

    return arr
        
s = input()
res = compress_str(s)
print(*res)