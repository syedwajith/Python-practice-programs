a = int(input())
count=1
for i in range(1,a*2):
    for j in range(1,a*2):
        if i<=a:
            if i==j or j+i==a*2:
                print(i,end=" ")
            else:
                print(" ",end=" ")
        else:
            if i==j or j+i==a*2:
                print(a-count+a,end=" ")
            else:
                print(" ",end=" ")
    count+=1
    print()


