class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for i in range(n):
            res = ""
            number = i+1
            if number % 3 == 0:
                res += "Fizz"
            if number % 5 == 0:
                res += "Buzz"
            if not res:
                res += str(number)
            r.append(res)
        return r