class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            t = 0
            while n > 0:
                p = n % 10
                n = (n-p) // 10
                t = t + (p**2)
            n = t
        return True


