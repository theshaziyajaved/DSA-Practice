class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        #Find the stones that are Jewels
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count
        
        