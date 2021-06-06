def two_sum(list, k):
    map = {}
    
    for n in list:
        if n in map:
            return map[n]
        map[k-n] = True
    return False

# True
print(two_sum([4,7,1,-3,2], 5))
# True
print(two_sum([4,7,1,-3,2], 1))
# False
print(two_sum([4,7,1,-3,2], 500))
# False
print(two_sum([4,7,1,-3,2], 12))
# True
print(two_sum([4,7,1,-3,2], 11))