class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        c = 0
        r = ""
        while i>=0 or j>=0 or c:
            bA = int(a[i] if i>= 0 else 0)
            bB = int(b[j] if j>= 0 else 0)
            t = bA + bB + c
            c = t // 2
            r = str(t%2) + r
            i -= 1
            j -= 1
        return r



        