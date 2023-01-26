from unicodedata import decimal


def test(x):
    a=int(x,2)
    print(a)
    count=0
    while a!=0:
        if a%2==0:
           a=a/2
        else:
            a=a-1
        count=count+1
    print(count)
bin=input()
test(bin)
