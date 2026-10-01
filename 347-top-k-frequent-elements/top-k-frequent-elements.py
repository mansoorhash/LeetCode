class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums
        from collections import Counter
        count = Counter(nums)
        return [i[0] for i in count.most_common(k)]
        

