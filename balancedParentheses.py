class Solution:
  def isValid(self, s):
    stack = []
    
    if s:
      mapping = {
        ')':'(',
        ']':'[',
        '}':'{'
      }
      
      for curr in s:
        if curr not in mapping:
          stack.append(curr)
        else:
          if len(stack) < 1 or mapping[curr] != stack.pop():
            return False
  
    return len(stack) ==  0

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = ")([{}])()"
# should return False
print(Solution().isValid(s))