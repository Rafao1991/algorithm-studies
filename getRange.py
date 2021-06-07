class Solution: 
  def getRange(self, arr, target):
    return_arr = [-1, -1]
    for i in range(len(arr)):
      if arr[i] == target:
        if arr[i - 1] != target:
          return_arr[0] = i
          return_arr[1] = i
        else:
          return_arr[1] = i
      
    return return_arr
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1,3,3,5,7,8,9,9,9,15]
x = 9
print(Solution().getRange(arr, x))
# [6,8]

arr = [100, 150, 150, 153]
x = 150
print(Solution().getRange(arr, x))
# [1,2]

arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))
# [-1, -1]

arr = [1,2,3,4,5,6,9]
x = 9
print(Solution().getRange(arr, x))
# [6, 6]