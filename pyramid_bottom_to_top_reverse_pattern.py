def pyramid(n):
    for i in range(n,0,-1):
        for j in range(n,i,-1):
            print(" ", end=" ")
        for k in range(i):
            print("*", end=" ")
        print()

no = int(input())
pyramid(no)