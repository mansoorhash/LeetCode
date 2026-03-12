class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r = 0
        for i, c in enumerate(columnTitle):
            v = ord(c) - 64
            r *= 26
            r += v*1
        return r