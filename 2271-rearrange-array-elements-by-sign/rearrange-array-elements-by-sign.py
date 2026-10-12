class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = 0
        neg = 0
        res = []
        while len(res) < len(nums):
            while nums[pos] < 0:
                pos += 1
            while nums[neg] > 0:
                neg += 1
            res.append(nums[pos])
            res.append(nums[neg])
            pos += 1
            neg += 1

        return res

            