class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp = sum(i for i in range(len(nums)+1))
        act = sum(i for i in nums)
        return exp - act