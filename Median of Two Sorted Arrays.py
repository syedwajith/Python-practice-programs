def findMedianSortedArrays(num1,num2):
    num3 = set()
    res = 0
    for i in range(len(num1)):
        num3.add(num1[i])
    for i in range(len(num2)):
        num3.add(num2[i])

    l1 = list(num3)
    if len(num3) % 2 == 1:
        res = len(num3) // 2
        return float(l1[res])
    else:
        first = (len(num3) // 2) - 1
        second = (len(num3) // 2) 
        res = (l1[first] + l1[second]) / 2
        return res
result1 = findMedianSortedArrays([1,3],[2])
result2 =findMedianSortedArrays([1,2],[3,4])
print(result1)
print(result2)