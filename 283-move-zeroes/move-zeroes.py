class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        l = 0
        r = 1
        size_n = len(nums) -1
        while l < size_n and l < r:
            if not nums[l]:
                while size_n > r and not nums[r]:
                    r += 1
                if r > size_n:
                    pass
                elif nums[r]:
                    move_n = nums[r]
                    nums[r] = nums[l]
                    nums[l] = move_n
            l += 1
            r = l + 1
        
                

