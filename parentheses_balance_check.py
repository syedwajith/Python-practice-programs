def isbalaced(s):
    stack = []
    for char in s:
        if char == '{' or char == '(' or char == '[':
            stack.append(char)
        else:
            if not stack:
                return False
            cur_char = stack.pop()
            if cur_char == '(':
                if char != ')':
                    return False
            elif cur_char == '{':
                if char != '}':
                    return False
            elif cur_char == '[':
                if char != ']':
                    return False
                
    if stack:
        return False
    return True

s = input()
res = isbalaced(s)
print(res)