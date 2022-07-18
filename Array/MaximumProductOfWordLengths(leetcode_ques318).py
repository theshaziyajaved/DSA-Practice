from ast import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_val = 0
        s = [set(words[i]) for i in range (len(words))]
        
        for i in range (len(words)):
            for j in range (i+1,len(words),1):
                if (s[i].isdisjoint(s[j]) == True):     #value of disjoint function                                                          is True only when there is                                                      nothing in common in s[i] and s[j]
                    max_val = max(max_val, len(words[i]) * len(words[j]))
        return (max_val)






class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_val = 0
        s = [set(words[i]) for i in range (len(words))]
        
        for i in range (len(words)):
            for j in range (i+1,len(words),1):
                if (s[i].intersection(s[j]) == set()):   #if there is no common                                                           letter in s[i] and s[j]
                    max_val = max(max_val, len(words[i]) * len(words[j]))
        return (max_val)