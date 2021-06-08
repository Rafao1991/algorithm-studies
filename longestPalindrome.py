class Solution: 
    def longestPalindrome(self, s):
      lp = 0
      rp = len(s) - 1
      start, end = lp, rp
      
      while lp <= rp:
        if s[lp] != s[rp]:
          if len(s[start:end+1]) % 2 == 0:
            rp -= 1
            end = rp
          else:
            lp += 1
            start = lp
        else:
          rp -= 1
          lp += 1
      
      return s[start:end+1]
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar

s = "xleveli"
print(str(Solution().longestPalindrome(s)))
# level

s = "xararajl"
print(str(Solution().longestPalindrome(s)))
# arara