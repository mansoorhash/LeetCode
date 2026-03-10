class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = []
        for n in range(rowIndex+1):
            row = [1]*(n+1)
            cr = r
            for nr in range(1,n):
                row[nr] = cr[nr-1] + cr[nr]
            r = row
        return r