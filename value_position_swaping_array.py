def swap_value(n):
    print("Input:")
    a=[]
    for i in range(n):
        b = list(map(int,input().split()))
        a.insert(i,b)
    print("Output:")
    row = len(a)
    col = len(a[0])
    for i in range(col):
        for j in range(row):
            print(a[j][i],end=" ")
        print()

n=int(input())
swap_value(n)