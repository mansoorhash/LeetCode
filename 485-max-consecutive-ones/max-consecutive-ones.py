class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0
        pr = 0
        for n in nums:
            if n == 1:
                pr += 1
            else: pr = 0
            r = max(pr, r)
        return r
                