def queen(n):
    even = 2
    odd = 1
    for i in range(n):
        for j in range(1,n+1):
            if 1<even<=n:
                if j==even:
                    print('Q',end=" ")
                else:
                    print('_', end=" ")
            else:
                if 0<odd<=n:
                    if j==odd:
                        print('Q',end=" ")
                    else:
                        print('_', end=" ")

        if i<n//2:
            even += 2
        else:
            odd += 2

        print()

n = int(input())
res = queen(n)