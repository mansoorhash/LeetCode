class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = 0
        l = 0
        r = len(nums) - 1
        while l < r:
            right_value = nums[r]
            value = nums[l] + nums[r]
            if value == k:
                res += 1
                l += 1
                r -= 1
            elif value > k:
                r -= 1
            else: l += 1
        return res