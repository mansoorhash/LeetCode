class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        s = 0
        count = {0: 1}
        result = 0
        for n in nums:
            s += n
            diff = s - k
            
            result += count.get(diff, 0)
            count[s] = count.get(s, 0) + 1
        return result
                