class Solution:
    def romanToInt(self, s: str) -> int:
        pair = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        r = 0
        for i in range(len(s)):
            if i + 1 < len(s) and pair[s[i]] < pair[s[i+1]]:
                r -= pair[s[i]]
            else:
                r += pair[s[i]]
                
        return r
