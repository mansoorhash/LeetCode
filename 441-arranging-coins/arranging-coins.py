class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        while r >= l:
            r -= l
            l += 1
        return l - 1