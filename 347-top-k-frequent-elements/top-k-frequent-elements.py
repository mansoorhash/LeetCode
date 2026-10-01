class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums
        from collections import Counter
        import heapq
        h = Counter(nums)
        res = []
        for n, count in h.items():
            heapq.heappush(res, (count, n))
            if len(res) > k:
                heapq.heappop(res)
        return [i[1] for i in res]
        

