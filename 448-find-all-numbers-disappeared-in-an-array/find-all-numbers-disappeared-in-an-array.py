class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        map = [0]*len(nums)

        for n in nums:
            map[n-1] = 1
        
        return [i+1 for i, n in enumerate(map) if n < 1]