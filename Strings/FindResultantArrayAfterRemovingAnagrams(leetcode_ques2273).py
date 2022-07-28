from ast import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        arr = []
        str1_ = ""
        
        for ele in words:
             x = sorted(ele)
             if x != str1_ :
                str1_ = x
                arr.append(ele)
        return arr
    
    
