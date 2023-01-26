n=int(input("Enter the value :"))
l1=[]
for i in range(0,n):
    l1.append(int(input("Enter the no:")))

print("list 1 :", l1)

l2=[]
for j in range(0,len(l1)):
    a=l1[j]%10
    b=l1[j]//10
    c=a+b
    l2.append(int(c))    
print("integer sum of list 1 :", l2)

sum=0
for k in range(0,len(l2)):
    sum=sum+l2[k]
print("sum of list 2 :", sum)
count=0
while sum>10:
    m=sum%10
    p=sum//10
    sum=m+p
    count+=1
print(sum)
print(f"while function executes {count} times")
