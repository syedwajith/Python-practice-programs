def removeelement(l,val):
    x = 0
    for i in l:
        if val != i:
            l[x] = i
            x += 1
    return x

res = removeelement([3,2,2,3],3)
print(res)