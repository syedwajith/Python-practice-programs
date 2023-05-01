def plus_pattern(n):
    for i in range(1,n):
        for j in range(1,n):
            if i == n//2 or j == n//2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

no = int(input())
plus_pattern(no)