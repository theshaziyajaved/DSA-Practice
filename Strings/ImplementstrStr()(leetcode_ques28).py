class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (len(needle))==0:
            return 0
        start = 0
        end = len(needle)
        
        while end <= len(haystack):
            if haystack[start:end] == needle:
                return start
            else:
                start = start+1
                end = end+1
        return -1
        
  
         