class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v = {}
        for i, n in enumerate(nums):
            s = target - n
            if s in v:
                return [v[s], i]
            v[n] = i
        return []