class Solution:
    def searchInsertK(self, Arr, N, k):
        n=len(Arr)
        for i in range (n):
            if (Arr[i]==k ):
                return i
            elif (Arr[i]>k):
                return (i)
        return (n)
        