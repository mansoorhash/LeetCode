class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        s = 0
        count = {0: 1}
        result = 0
        for n in nums:
            s += n
            result += count.get(s - k, 0)
            count[s] = count.get(s, 0) + 1
        return result
                