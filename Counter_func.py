from collections import Counter
# Example 1
str = "aaavddffgghhhjkkeskskksksss"
c = Counter(str)
print(c)

# Example 2
str1 = {'a':5, 'b':5}
c2 = Counter(str1)
print(list(c2.elements()))