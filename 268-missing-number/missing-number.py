class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s = {i for i in range(len(nums)+1)}
        for n in nums:
            if n in s:
                s.discard(n)
        v = [i for i in s]
        return v[0]