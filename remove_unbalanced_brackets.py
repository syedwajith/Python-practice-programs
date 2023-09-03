def rem_par(s):
    stack = []
    final_val = ""
    current_str = ""
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                current_par = stack.pop()

            if i == ')':
                if len(current_str) == 0:
                    final_val = current_par + final_val + i
                else:
                    final_val += current_par + current_str + i
                    current_str = ""
            else:
                current_str += i 

    return final_val

s = input()
res = rem_par(s)
print(res)