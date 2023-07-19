from itertools import permutations

# Using permutations class

def permutation(arr):
    if len(arr)<3:
        for i in range(len(arr)-1):
            res = list(permutations(arr[i],int(arr[i+1])))
    else:
        return "Please provide valid input"
    
    return res

my_arr = list(map(str, input().split()))
result = permutation(my_arr)
print(result)