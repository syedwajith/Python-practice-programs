from audioop import reverse

# using loop by calling function

s=input("enter the string :")
def reverse(s):
    str=""
    for i in s:
        str=i+str
    print(str)

reverse(s)

# directly reverse the string

var = str(input())[::-1]
print(var)



