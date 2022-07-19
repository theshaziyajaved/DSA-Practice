
class Solution:
    def oddAndEven(self,S):
        odd,even =0,0
        for i in range(len(S)):
            if i%2 == 0:
                even += int(S[i])
            else:
                odd += int(S[i])
        return 1 if even==odd else 0  

