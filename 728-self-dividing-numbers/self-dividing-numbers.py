class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r = []
        for n in range(left, right+1):
            v = n
            while v != 0:
                d = v % 10
                v //= 10
                if d == 0 or ((n/d) % 1) != 0:
                    break
            else:
                r.append(n)
        return r


