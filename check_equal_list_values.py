n = int(input())
l1 = []

for i in range(0,n):
    a = int(input())
    for j in range(0,a):
        l1.append(int(input()))
print(l1)

s = []
w = 1
for k in range(0,len(l1)):
    if l1[k]!=w:
        s.append(l1[k]-1)
    else:
        s.append(l1[k])
print(s)

c = s[0]
for m in range(0,len(s)):
    if s[m]==c:
        c=s[m]
print("1")