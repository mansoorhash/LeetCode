class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        from collections import Counter

        count = Counter(nums)
        missing = []

        for n in range(len(nums)):
            val = n+1
            if val not in count:
                missing.append(val)
        return missing