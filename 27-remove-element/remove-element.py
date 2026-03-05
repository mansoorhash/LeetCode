class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for n in nums:
            if n != val:
                nums[x] = n
                x += 1
        return x