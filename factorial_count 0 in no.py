n=int(input())
v=1
for i in range(1,n+1):
    v=v*i
print(v)
x=str(v)
count=0
for j in x:
    if j=='0':
        count+=1
print(count)