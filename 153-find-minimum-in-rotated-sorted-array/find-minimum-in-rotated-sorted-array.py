class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) -1

        result = float("inf")
        while l <= r:
            mid = l + (r-l) // 2
            if nums[l] <= nums[mid]:
                if nums[r] < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] < nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            result = min(result, nums[mid])
        return result