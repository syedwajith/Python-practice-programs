def maxoflist():
    n  = int(input())
    list = []
    for i in range(n):
        list.append(input())
    
    list2 = []
    for i in range(n):
        sum = 0
        for j in range(len(list[i])):
            sum += int(list[i][j])
        list2.append(sum)
    
    max = list2[0]
    for i in range(1,n):
        if max < list2[i]:
            max = list2[i]
    print(max)
maxoflist()

