from collections import defaultdict

str = ['str','str','strr','aed']
d = defaultdict(list)

for i in str:
    d[i].append(i)
    
print(d)
