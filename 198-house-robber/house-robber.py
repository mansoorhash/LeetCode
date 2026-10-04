class Solution:
    def rob(self, nums: list[int]) -> int:
        idx0 = 0
        idx1 = 0

        for n in nums:
            idx0, idx1 = idx1, max(n+idx0, idx1)
            
        return idx1