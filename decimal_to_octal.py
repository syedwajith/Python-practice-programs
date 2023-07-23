# using in-build function

n = int(input())
n = oct(n)
n1 = ""
for i in range(len(n)):
    if i == 0 or i == 1:
        continue
    else:
        n1 += n[i]
print(n1)

# without using in-build function

def dec_oct(n):
    octal = []

    while n != 0:
        oct_val = n % 8
        octal.append(oct_val)
        n = n // 8

    for i in range(len(octal)-1, -1, -1):
        print(octal[i],end="")

n = int(input())
res = dec_oct(n)