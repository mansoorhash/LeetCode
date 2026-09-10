class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls = len(s)
        for i in range(1, ls//2+1):
            sRange = s[:i]
            multiple = ls // len(sRange)
            if multiple*sRange == s:
                return True
        return False
