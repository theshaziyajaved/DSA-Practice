#finding max element and returning the index of max element
class Solution:   
    def peakElement(self,arr, n):
        maxEle = max(arr)
        return arr.index(maxEle)