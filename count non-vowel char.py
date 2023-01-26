n=int(input())
l1=[]
for i in range(0,n):
    l1.append(input())

count=0
for j in range(0,n):
    if l1[j]!='a' and l1[j]!='e' and l1[j]!='i' and l1[j]!='o' and l1[j]!='u' and l1[j]!='A' and l1[j]!='E' and l1[j]!='I' and l1[j]!='O' and l1[j]!='U':
        count+=1
        
print(count)