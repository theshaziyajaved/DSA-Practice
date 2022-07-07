class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        n= len(res)
        l = 0
        r = n-1
        arr = []
        string = " "
        while (l<=r):
            arr.append(res[r])
            r = r-1
        
        for i in range (len(arr)):
            string += arr[i]+ " "
        return (string.strip())





class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        string = " "
        n = len(res)
        for i in range (n-1,-1,-1):
            string += res[i] + " "
        return (string.strip())
  
        