class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1 and n != 1: return False
        def recursion(n):
            number=n/2
            if number >1:
                number = recursion(number)
            return number
        return (recursion(n) == 1) if n > 1 else True