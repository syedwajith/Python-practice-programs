# using in-build function

n = int(input())
n = bin(n)
n1 = ""
for i in range(len(n)):
    if i == 0 or i == 1:
        continue
    else:
        n1 += n[i]
print(n1)

# without using in-build function

def dec_bin(n):
    binary = []

    while n != 0:
        bin_val = n % 2
        binary.append(bin_val)
        n = n // 2

    for i in range(len(binary)-1, -1, -1):
        print(binary[i],end="")

n = int(input())
res = dec_bin(n)