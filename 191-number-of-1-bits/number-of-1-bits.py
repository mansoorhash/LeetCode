class Solution:
    def hammingWeight(self, n: int) -> int:
        r = 0
        for _ in range(32):
            if (n&1) == 1: r+=1
            n >>= 1
        return r