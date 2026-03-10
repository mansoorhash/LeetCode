class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = []
        for n in range(numRows):
            row = [1] * (n + 1)
            for nr in range(1,n):
                row[nr] = r[n-1][nr-1] + r[n-1][nr]
            r.append(row)
        return r
