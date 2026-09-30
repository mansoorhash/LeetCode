class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for n in nums:
            heap.append(-n)
        heapq.heapify(heap)
        for _ in range(k-1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)