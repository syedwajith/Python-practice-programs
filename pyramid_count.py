'''
n = 1
/\ 
o/p: 2

n = 2
 /__\
/\  /\
o\p: 7
'''
def per(n):
    if n == 0:
        return -1
    
    count = 0
    for i in range(1,n+1):
        for j in range(1,i*3):
            count += 1
    return count

n = int(input())
res = per(n)
print(res)