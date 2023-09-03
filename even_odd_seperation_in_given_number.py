def even_odd_display(n, eo):
    even = 0
    odd = 0
    even1 = 0
    odd1 = 0

    while n > 0:
        rem = n % 10
        if rem % 2 == 0:
            even = (even * 10) + rem
        else:
            odd = (odd * 10) + rem
        n = n // 10
    
    while even > 0 :
        rem = even % 10
        even1 = (even1 * 10) + rem
        even = even // 10

    while odd > 0:
        rem = odd % 10
        odd1 = (odd1 * 10) + rem
        odd = odd // 10
    
    if eo == 0:
        print(f"{even1}{odd1}")
    else:
        print(f"{odd1}{even1}")

n = int(input())
eo = int(input())
res = even_odd_display(n, eo)