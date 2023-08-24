def palindromeIndex(s):
    rev_str = s[::-1]
    if s == rev_str:
        return True
    else:
        for i in range(len(s)):
            new_str = s[:i] + s[i+1:]
            rev = new_str[::-1]
            if new_str == rev:
                return i
        return None

s = input().strip()
res = palindromeIndex(s)
print(res)
