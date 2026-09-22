class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        bal = 0
        for char in s:
            if char == "R":
                bal += 1
            else: 
                bal -=1
            if bal == 0: 
                c += 1
        return c
        