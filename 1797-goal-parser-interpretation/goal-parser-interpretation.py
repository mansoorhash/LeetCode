class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        l = 0
        while l < len(command):
            if command[l] == "G": res += "G"
            elif command[l] == "(":
                l += 1
                if command[l] == ")":
                    res += 'o'
                elif command[l:l+3] == "al)":
                    res += 'al'
            l += 1
        return res