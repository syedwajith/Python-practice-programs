def cross_pattern(s):
    n = len(s)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j or i+j==n+1:
                print(s[j-1], end=" ")
            else:
                print(" ", end=" ")

        print()

s = input()
res = cross_pattern(s)