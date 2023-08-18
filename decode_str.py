'''
input : 3[a]2[bc]
output : aaabcbc

input : 3[a2[bc]]
output : abcbcabcbcabcbc
'''

def decode_str(s):
    stack = []
    current_num = 0
    current_str = ""
    for i in s:
        if i.isdigit():
            current_num = current_num + int(i)
        elif i == '[':
            stack.append((current_num,current_str))
            current_num = 0
            current_str = ""
        elif i == ']':
            num, prev_str = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += i

    return current_str

s = input()
res = decode_str(s)
print(res)