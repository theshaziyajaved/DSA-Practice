class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        str = ""
        for i in range (n):
            if (command[i] == "G"):
                str += "G"
            elif (command[i] == "(" and command[i+1] == ")" ):
                str += "o"
            elif (command[i] == "(" and command[i+1] == "a" and command[i+2] == "l" and command[i+3] == ")" ):
                str += "al"
        return str