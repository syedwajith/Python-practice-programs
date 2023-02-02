def addtwolist(l1,l2):
    l3 = []
    str_l1 = ""
    str_l2 = ""
    for i in range(len(l1)):
        str_l1 = str(l1[i]) + str_l1
    #print(str_l1)

    for j in range(len(l2)):
        str_l2 = str(l2[j]) + str_l2
    #print(str_l2)

    res = str(int(str_l1) + int(str_l2))[::-1]
    #print(res)
    for i in res:
        l3.append(int(i))
    return l3
result = addtwolist([9,9,9,9,9,9,9],[9,9,9,9])
print(result)