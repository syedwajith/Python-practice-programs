def same_char(s):
    min_len_str = s[0]
    for i in range(1, len(s)):
        if len(min_len_str) > len(s[i]):
            min_len_str = s[i]
    
    a = False
    new_str = ""
    col = len(min_len_str)
    row = len(s)
    for i in range(col):
        char = min_len_str[i]
        for j in range(row):
            if char == s[j][i]:
                continue
            else:
                a = True
                break
        if a:
            break
        else:
            new_str += char

    return new_str

s = list(map(str, input().split()))
res = same_char(s)
print(res)