class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = set(nums)
        missing = []

        for n in range(len(nums)):
            val = n+1
            if val not in count:
                missing.append(val)
        return missing