'''
Testcase 1 :

    Input : a1s2

    Output : ass

Testcase 2 :

    Input : sa2f3

    Output : sasafff

'''

def decode_str(s):
    current_str = ""
    final_str = ""

    for i in s:
        if i.isdigit():
            final_str =  final_str + (current_str * int(i))
            current_str = ""
        else:
            current_str += i

    return final_str

s = input()
res = decode_str(s)
print(res)