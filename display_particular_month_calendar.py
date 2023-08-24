from calendar import *

def cal(y,m):
    p = TextCalendar(6)
    cal = p.formatmonth(y,m)
    return cal

y = int(input("Year : "))
m = int(input("Month : "))
res = cal(y,m)
print(res)