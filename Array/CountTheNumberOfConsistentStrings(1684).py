class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        str = "".join(sorted(allowed))
        count=0
        for i in words:
            x = "".join(sorted(set(i + str)))
            if str == x:
                count +=1
        return count