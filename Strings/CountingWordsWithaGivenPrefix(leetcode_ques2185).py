from ast import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in range (len(words)):
            if words[i].startswith(pref):
                count += 1
        return count
    



class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
	    for ele in words:
            if pref == ele[0:len(pref)]:
                count +=1
	    return count    
                
        

