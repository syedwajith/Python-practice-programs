decnum = int(input())
bin = bin(decnum)[2:]
print(bin)
n = ""
for i in bin:
    if i=='0':
        continue
    else:
        n+=i
print(n)
a = int(n,2)
print(a)