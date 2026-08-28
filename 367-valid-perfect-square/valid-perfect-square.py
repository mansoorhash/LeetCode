class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        l = 1
        r = num // 2
        while l <= r:
            mid = l + (r-l) //2
            ans = mid*mid
            print(ans, mid)
            if ans == num:
                return True
            elif ans < num:
                l = mid + 1
            elif ans > num:
                r = mid - 1
        return False
        