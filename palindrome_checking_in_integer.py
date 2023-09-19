def palindrome(n):
    if n < 10:
        return False
    
    rev = 0
    n1 = n
    while n1 > 0:
        rem = n1 % 10
        rev = (rev * 10) + rem
        n1 = n1 // 10 

    if n == rev:
        return True
    else:
        return False

n = int(input())
res = palindrome(n)
print(res)