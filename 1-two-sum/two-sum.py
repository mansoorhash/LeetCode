class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, n in enumerate(nums):
            sum = target - n
            if sum in nums and nums.index(sum) != i:
                return [i, nums.index(sum)] 
