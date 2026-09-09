class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]

        l = 0
        r = len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] == target:
                res[0] = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l = 0
        r = len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] == target:
                res[1] = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res