l1 = [1,2,3,4,5,6]
l = len(l1)
first_half = []
second_half = []
ans = []

for i in range(0,l//2):
    first_half.append(l1[i])
first_rev = first_half[::-1]
print(first_half)
print(first_rev)

for j in range(l//2,l):
    second_half.append(l1[j])
print(second_half)

for k in range(0,l//2):
    mult = first_rev[k] * second_half[k]
    ans.append(mult)
print(ans)

