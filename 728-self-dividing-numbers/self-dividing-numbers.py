class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []
        for n in range(left, right+1):
            skip = False
            if n % 10 == 0:
                continue
            v = n
            while v != 0:
                d = v % 10
                v //= 10

                if d == 0 or ((n/d) % 1) != 0:
                    skip = True
            if not skip:
                r.append(n)
        return r


