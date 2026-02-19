class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums
        v = {}
        for n in nums:
            v[n] = v.get(n, 0) + 1
        indexPos = [[] for _ in range(len(nums)+1)]
        print(v, indexPos)
        for val, idx in v.items():
            indexPos[idx].append(val)
        size = len(nums)
        result = []
        for step in range(size, -1, -1):
            for idx in indexPos[step]:
                result.append(idx)
                if len(result) == k: return result