class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r = []
        while columnNumber > 0:
            columnNumber -= 1
            c = columnNumber%26
            r.append(chr(65+c))
            columnNumber = int(columnNumber/26)
        
        return ''.join(r[::-1])