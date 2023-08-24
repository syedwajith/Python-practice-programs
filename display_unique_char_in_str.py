def uniq_char(s):
    uniq = ""
    for i in s:
        count = 0
        for j in s:
            if i == j:
                count += 1
        if count == 1:
            uniq += i
    return uniq

s = input("Enter a String : ")
res = uniq_char(s)
print(res)