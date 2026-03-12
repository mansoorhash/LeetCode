class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f = {}
        b = int()
        for n in nums:
            f[n] = f.get(n,0) + 1
            if not b:
                b = n
            if n != b and f[n] > f[b]:
                b = n
        return b
