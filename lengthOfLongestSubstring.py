class Solution:
  def lengthOfLongestSubstring(self, s):
    if not s:
        return 0
    
    i1 = 0
    i2 = i1 + 1
    mapping = {}
    max_sub_len = 0
    
    while i1 < len(s):
      if i2 >= len(s):
        i1 += 1
        i2 = i1 + 1
        continue
      else:
        if i1 not in mapping:
          if s[i1] != s[i2]:
            mapping[i1] = s[i1] + s[i2]
          else:
            i1 += 1
            i2 = i1 + 1
            continue
        else:
          if s[i2] not in mapping[i1]:
            mapping[i1] += s[i2]
          else:
            if len(mapping[i1]) > max_sub_len:
              max_sub_len = len(mapping[i1])
            i1 += 1
            i2 = i1 + 1
            continue  
        i2 += 1
    
    return max_sub_len

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10

print(Solution().lengthOfLongestSubstring('abrkaabcdefghiijjxxx'))
# 9