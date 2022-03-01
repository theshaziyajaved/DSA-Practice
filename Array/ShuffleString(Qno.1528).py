from ast import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr= ['']*len(s)
        str1=""
        for i in range (len(s)):
            arr[indices[i]] = s[i]
            str1= ''.join(arr)
        return str1
    

    
    