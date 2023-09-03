def leap_or_not(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 100 == 0 and y % 400 == 0):
        return True
    else:
        return False

y = int(input())
res = leap_or_not(y)
print(res)