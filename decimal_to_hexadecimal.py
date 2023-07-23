# using in-build function

n = int(input())
n = hex(n)
n1 = ""
for i in range(len(n)):
    if i == 0 or i == 1:
        continue
    else:
        n1 += n[i]
print(n1)

# without using in-build function

def dec_hexa(n):
    hexa = []

    while n != 0:
        hex_val = n % 16
        hexa_val = gethexachar(hex_val)
        hexa.append(hexa_val)
        n = n // 16

    for i in range(len(hexa)-1, -1, -1):
        print(hexa[i],end="")

def gethexachar(hex_val):
    if hex_val < 10:
        return hex_val
    elif hex_val == 10:
        return 'A'
    elif hex_val == 11:
        return 'B'
    elif hex_val == 12:
        return 'C'
    elif hex_val == 13:
        return 'D'
    elif hex_val == 14:
        return 'E'
    elif hex_val == 15:
        return 'F'

n = int(input())
res = dec_hexa(n)