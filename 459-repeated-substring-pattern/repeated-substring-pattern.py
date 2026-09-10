class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls = len(s)
        for i in range(1, ls//2+1):
            sRange = s[:i]
            if ls%i != 0: continue

            multiple = ls // i

            if sRange * multiple == s:
                return True
        return False
