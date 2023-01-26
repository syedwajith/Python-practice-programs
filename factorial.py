# using function and conditions

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
a=int(input())

print(fact(a))

# using loop

n=int(input())
v=1
for i in range(1,n+1):
    v=v*i
print(v)