def sortNums(nums):
    return_arr = []
    sort_dict = {}
    
    # O(n)
    for n in nums:
        if n not in sort_dict:
            sort_dict[n] = 1
        else:
            sort_dict[n] += 1
    
    max, min = 0, 9999        
    # O(3)
    for n in sort_dict.keys():
        if n > max:
            max = n
        elif n < min:
            min = n
         
    # O(n)
    for n in range(sort_dict[min]):
        return_arr.append(min)
    
    # O(n)
    for n in range(sort_dict[max - 1]):
        return_arr.append(max - 1)

    # O(n)        
    for n in range(sort_dict[max]):
        return_arr.append(max)
    
    return return_arr

# Given a list of numbers with only 3 unique numbers (1, 2, 3)
print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
print(sortNums([2, 3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 2, 3, 3, 3]
print(sortNums([92, 93, 93, 92, 91, 93, 92, 91]))
# [91, 91, 92, 92, 92, 93, 93, 93]