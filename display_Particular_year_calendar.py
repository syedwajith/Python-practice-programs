from calendar import *

def cal(y):
    p = TextCalendar(6)
    cal = p.formatyear(y)
    return cal

y = int(input())
res = cal(y)
print(res)