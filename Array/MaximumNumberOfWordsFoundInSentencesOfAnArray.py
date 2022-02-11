from ast import List
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        n=len(sentences)
        count=0
        for i in range (n):
            str=sentences[i]
            res=len(str.split())
            if (res > count):
                count=res
            
        i=i+1
        return (count)
       